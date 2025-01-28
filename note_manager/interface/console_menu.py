import datetime
import sqlite3
from random import choice

from note_manager.config import CONFIG
from .filters_menu import filters_menu
from .error_handling_ui import handle_error
from note_manager.data.database import save_note_to_db, load_notes_from_db,setup_database, update_note_in_db, delete_note_from_db
from .color_output import display_notes_with_colors, display_issue_note
from note_manager.reports.export import export_notes_to_file

def display_page(notes, page, notes_per_page=3):
    start = (page - 1) * notes_per_page
    end = start + notes_per_page
    page_notes = notes[start:end]

    print(f"\n=== Страница {page} ===")
    for note in page_notes:
        display_notes_with_colors(note)
    print("\n[N] Следующая страница | [P] Предыдущая страница | [Q] Выход")

def paginate_notes(notes):
    page = 1
    notes_per_page = 3
    total_pages = (len(notes) + notes_per_page - 1) // notes_per_page

    while True:
        display_page(notes, page, notes_per_page)
        choice = input("Ваш выбор: ").strip().lower()

        if choice == "n" and page < total_pages:
            page += 1
        elif choice == "p" and page > 1:
            page -= 1
        elif choice == "q":
            print("Выход из навигации.")
            break
        else:
            handle_error("invalid_input")

def display_notes(notes, in_pages = False, note_is_not_found = False):  # функция которая выводит всё содержимое списка заметок
    if notes == []:
        if note_is_not_found == False:
            handle_error("empty_list")
        else:
            print('=== Подходящие заметки не найдены ===')
        print('-' * 28)
    else:
        print('Список заметок:')
        print('-' * 28)
        if in_pages == True:
            paginate_notes(notes)
        else:
            for i, note in enumerate(notes, start=1):
                print(f'Заметка №{i}')
                display_notes_with_colors(note)

def menu():

    def convert(user_input): #конвертирует ввод пользователя в int
        try:
            return int(user_input)
        except ValueError:
            raise ValueError(
                "Некорректный ввод, введите число соответсвующее номеру")

    def parse_date(user_input):  # функция которая переводит ввод пользователя в datetime
        try:
            return datetime.datetime.strptime(user_input, CONFIG['DATE_FORMAT']).date()
        except ValueError:
            raise ValueError(
                "Некорректный формат даты. Убедитесь, что вводите дату в формате день-месяц-год (например, 10-12-2024).")

    def create_note():  # функция которая добавляет в список заметку ввиде словаря

        current_date = datetime.date.today().strftime(CONFIG['DATE_FORMAT'])  # получаем текущую дату и заносим её в переменную

        note = {'id' : None,'username': input("Введите имя пользователя: "), 'title': input("Введите заголовок заметки: "),
                'content': input("Введите описание заметки: "), 'status': input("Введите статус заметки: "),
                'created_date': current_date,
                'issue_date': None}

        while True:  # создаём цикл который будет получать дату дедлайна от пользователя, и если ввод неверный выводить сообщение и повторять запрос
            user_input = input("Введите дату дедлайна (в формате день-месяц-год): ")
            try:
                issue_date = parse_date(user_input)
                break
            except ValueError as e:
                print(e)
        note['issue_date'] = issue_date.strftime(CONFIG['DATE_FORMAT'])  # не забываем добавить дедлайн в заметку
        save_note_to_db(note, CONFIG['DB_PATH']) # сохраняем заметку в базу данных
        return note

    def update_note(notes):  # функция которая обновляет выбранное поле
        print('Выберите какую заметку редактировать')
        display_notes(notes)
        while True:
            user_choice = input('Ваш выбор: ')
            try:
                note_to_update = convert(user_choice) - 1
                if note_to_update == len(notes):
                    handle_error("note_not_found")
                    continue
                elif note_to_update > len(notes) or note_to_update < 0:
                    handle_error("note_not_found")
                    continue
                else:
                    print('Введите новые значения(или оставьте пустым для того, чтобы не изменять)')
                    while True:  # создаём цикл который выводит доступные для изменения поля на экран, а если поле не доступно или отсутсвует, то сообщает об этом
                        updates = {'username': input("Введите новое имя пользователя: "), 'title': input("Введите новый заголовок заметки: "),
                                   'content': input("Введите новое описание заметки: "),'status': input("Введите новый статус заметки: "),'issue_date': ''}
                        while True:  # создаём цикл который будет получать дату дедлайна от пользователя, и если ввод неверный выводить сообщение и повторять запрос
                            user_input = input("Введите новую дату дедлайна (в формате день-месяц-год): ")
                            if user_input == '':
                                break
                            try:
                                new_issue_date = parse_date(user_input)
                                updates['issue_date'] = new_issue_date.strftime(CONFIG['DATE_FORMAT'])  #не забываем добавить дедлайн в заметку
                                break
                            except ValueError as e:
                                print(e)
                        break
                    for i in updates.keys():
                        if updates[i] == '':
                            updates[i] = notes[note_to_update][i]
                            continue
                        notes[note_to_update][i] = updates[i]
                    update_note_in_db(notes[note_to_update]['id'], updates, CONFIG['DB_PATH'])
                    break
            except ValueError as e:
                print(e)


    def delete_note(notes):
        while True:
            note_to_delete = []  # создаём список в который мы выносим индексы тех заметок которые нужно удалить
            user_answer = input('Хотите удалить заметку? (да/нет): ')  # спрашиваем пользователя об удалении
            if user_answer == 'да' and notes != []:
                user_choose = input('Введите имя пользователя или заголовок для удаления заметки: ')
                before_delite = len(notes)  # создаём переменную для того что бы увидеть изменился ли размер списка(были ли удалены некоторые элементы)
                for note in notes:
                    if note['username'] == user_choose:
                        note_to_delete.append(note)
                    elif note['title'] == user_choose:
                        note_to_delete.append(note)
                for i in note_to_delete:
                    notes.remove(i)  # удаляем те заметки чьи индексы мы занесли в список note_to_delete
                    delete_note_from_db(i['id'], CONFIG['DB_PATH'])
                if before_delite == len(notes):
                    handle_error("note_not_found")  # если размер списка не изменился, то сообщаем что такой заметки нет
                else:
                    print(
                        'Успешно удалено. Остались следующие заметки:')  # раз размер списка изменился то и удаление прошло успешно, сообщаем об этом пользователю
                    display_notes(notes)  # выводим оставшиеся заметки
                continue
            if user_answer == 'да':
                display_notes(notes)
            elif user_answer == 'нет':  # выходим из цикла
                break
            else:  # если ввод неверный повторяем запрос
                handle_error("invalid_input")
                continue

    def search_notes(notes):
        display_notes(filters_menu(notes), note_is_not_found = True)

    def check_reminders(db_path):
        notes = load_notes_from_db(db_path)
        reminders = [note for note in notes if datetime.datetime.strptime(note['issue_date'], CONFIG['DATE_FORMAT']).date() < datetime.date.today()]

        if reminders:
            print("\n=== Напоминания ===")
            for note in reminders:
                display_issue_note(note)
                print('----------------------------')
        else:
            print("🔔 Нет заметок с истёкшими дедлайнами.")

    def export_notes(notes):
        while True:
            choice = input('Введите формат экспорта\n1 - ".txt"\n2 - ".json"\nВаш выбор: ')
            if choice == '1':
                export_notes_to_file(notes, f'{CONFIG['EXPORT_PATH']}notes.txt')
                break
            elif choice == '2':
                export_notes_to_file(notes,f'{CONFIG['EXPORT_PATH']}notes.json')
                break
            else:
                handle_error("invalid_input")
                continue


    try:
        note_list = load_notes_from_db(CONFIG['DB_PATH']) #вызываем функцию для загрузки заметок
    except sqlite3.OperationalError:
        print('База данных не найдена. Создана новая.')
        setup_database(CONFIG['DB_PATH'])
        note_list = []
    print('Добро пожаловать в менеджер заметок!')
    while True:
        print(
            '\nМеню действий: \n1. Создать новую заметку\n2. Показать все заметки\n3. Обновить заметку\n4. Удалить заметку'
            '\n5. Найти заметки\n6. Показать напоминания\n7. Экспортировать заметки в файл\n8. Выйти из программы')
        user_commande = input('Ваш выбор(введите номер команды): ')

        if user_commande == '1': #вызываем функцию в зависимости от выбранной комманды
            note_list.append(create_note())
            continue
        elif user_commande == '2':
            display_notes(note_list, True)
            continue
        elif user_commande == '3':
            if note_list != []:
                update_note(note_list)
                continue
            else:
                display_notes(note_list)
                continue
        elif user_commande == '4':
            if note_list != []:
                delete_note(note_list)
                continue
            else:
                display_notes(note_list)
                continue

        elif user_commande == '5':
            if note_list != []:
                search_notes(note_list)
                continue
            else:
                display_notes(note_list)
                continue
        elif user_commande == '6':
            if note_list != []:
                check_reminders(CONFIG['DB_PATH'])
                continue
            else:
                display_notes(note_list)
                continue
        elif user_commande == '7':
            if note_list != []:
                export_notes(note_list)
                continue
            else:
                display_notes(note_list)
                continue
        elif user_commande == '8':
            break
        else:  # если ввод неверный повторяем запрос
            handle_error("invalid_input")
            continue