import datetime
import sqlite3

from notes_data import save_note_to_db, load_notes_from_db,setup_database, update_note_in_db, delete_note_from_db
from pagination import paginate_notes
from filters_menu import filters_menu
from error_handling_ui import handle_error
from color_output import display_notes_with_colors

def display_notes(notes, in_pages = False):  # функция которая выводит всё содержимое списка заметок
    if notes == []:
        handle_error("empty_list")
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
            return datetime.datetime.strptime(user_input, '%d-%m-%Y').date()
        except ValueError:
            raise ValueError(
                "Некорректный формат даты. Убедитесь, что вводите дату в формате день-месяц-год (например, 10-12-2024).")

    def create_note():  # функция которая добавляет в список заметку ввиде словаря

        current_date = datetime.date.today().strftime('%d-%m-%Y')  # получаем текущую дату и заносим её в переменную

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
        note['issue_date'] = issue_date.strftime('%d-%m-%Y')  # не забываем добавить дедлайн в заметку
        save_note_to_db(note, 'notes.db') # сохраняем заметку в базу данных
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
                                updates['issue_date'] = new_issue_date.strftime('%d-%m-%Y')  #не забываем добавить дедлайн в заметку
                                break
                            except ValueError as e:
                                print(e)
                        break
                    for i in updates.keys():
                        if updates[i] == '':
                            updates[i] = notes[note_to_update][i]
                            continue
                        notes[note_to_update][i] = updates[i]
                    update_note_in_db(notes[note_to_update]['id'], updates, 'notes.db')
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
                    delete_note_from_db(i['id'], 'notes.db')
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
        if filters_menu(notes):
            display_notes(filters_menu(notes))

    try:
        note_list = load_notes_from_db('notes.db') #вызываем функцию для загрузки заметок
    except sqlite3.OperationalError:
        print('Файл notes.db не найден. Создан новый файл.')
        setup_database('notes.db')
        note_list = []
    print('Добро пожаловать в менеджер заметок!')
    while True:
        print(
            '\nМеню действий: \n1. Создать новую заметку\n2. Показать все заметки\n3. Обновить заметку\n4. Удалить заметку\n5. Найти заметки\n6. Выйти из программы')
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
            break
        else:  # если ввод неверный повторяем запрос
            handle_error("invalid_input")
            continue

if __name__ == "__main__":
    menu()