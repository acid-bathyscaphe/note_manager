import datetime
from itertools import repeat

def convert(user_input):
    try:
        return int(user_input)
    except ValueError:
        raise ValueError(
            "Некорректный ввод, введите число соответсвующее номеру")

def parse_issue_date(user_input): #функция которая переводит ввод пользователя в datetime
    try:
        return datetime.datetime.strptime(user_input, '%d-%m-%Y').date()
    except ValueError:
        raise ValueError(
            "Некорректный формат даты. Убедитесь, что вводите дату в формате день-месяц-год (например, 10-12-2024).")

def create_note():  # функция которая добавляет в список заметку ввиде словаря

    current_date = datetime.date.today().strftime('%d-%m-%Y')  # получаем текущую дату и заносим её в переменную

    note = {'Имя': input("Введите имя пользователя: "), 'Заголовок': input("Введите заголовок заметки: "),
             'Описание': input("Введите описание заметки: "), 'Статус': input("Введите статус заметки: "),
             'Дата создания': current_date,
             'Дедлайн': None}

    while True:  # создаём цикл который будет получать дату дедлайна от пользователя, и если ввод неверный выводить сообщение и повторять запрос
        user_input = input("Введите дату дедлайна (в формате день-месяц-год): ")
        try:
            issue_date = parse_issue_date(user_input)
            break
        except ValueError as e:
            print(e)
    note['Дедлайн'] = issue_date.strftime('%d-%m-%Y') #не забываем добавить дедлайн в заметку
    return note

def display_notes(notes): #функция которая выводит всё содержимое списка заметок
    print('Список заметок:')
    print('-' * 15)
    if notes == []:
        print("Заметок нет")
    else:
        for i in range(0, len(notes)):
            print(i + 1)
            for j, k in notes[i].items():
                print(j, ':', k)
            print('-' * 15)

def search_notes(notes, keyword=None, status=None):
    note_to_show = []
    is_finded = False
    for i in range(0, len(notes)):

        for j, k in notes[i].items():

            if k == keyword or k == status:
                print(j)
                note_to_show.append(notes[i])
                is_finded = True
    if is_finded == True:
        display_notes(note_to_show)
    else:
        print('Заметки, соответствующие запросу, не найдены')

def update_note(note): #функция которая обновляет выбранное поле

    while True: #создаём цикл который выводит доступные для изменения поля на экран, а если поле не доступно или отсутсвует, то сообщает об этом
        user_choose = input(f'Какие данные вы хотите обновить? {note.keys()}: ')
        is_changed = False #булевая переменная которая нужна для выхода из цикла

        for i in note:

            if user_choose == i:

                if i == 'Дата создания':
                    print('Данные неизменяемы')
                    break

                elif i == 'Дедлайн':

                    while True:  #создаём цикл который будет получать дату дедлайна от пользователя, и если ввод неверный выводить сообщение и повторять запрос
                        user_input = input()
                        try:
                            issue_date = parse_issue_date(user_input).strftime('%d-%m-%Y') #Заносим полученый результат в переменную заранее приведя к нужному формату
                            break
                        except ValueError as e:
                            print(e)
                    note[i] = issue_date #Заменяем нужное значение
                    is_changed = True
                    break

                else:
                    note[i] = input('Введите новое значение: ') #Заменяем нужное значение
                    is_changed = True
                    break

        if is_changed == True: #Если значение было изменено, то is_changed должна равняться True(см. line51, line55) и мы выходим из цикла
            break

        print('Неверный ввод(Ошибка в названии/Такого имени нет/Данные не доступны для изменения)') #Если ввод был неверным сообщаем об этом пользователю
        continue
    return note #Функция возвращает исправленную заметку

def delete_note(notes):
    while True:
        note_to_delete = []  # создаём список в который мы выносим индексы тех заметок которые нужно удалить
        user_answer = input('Хотите удалить заметку? (да/нет): ')  # спрашиваем пользователя об удалении
        if user_answer == 'да':
            user_choose = input('Введите имя пользователя или заголовок для удаления заметки: ')
            before_delite = len(notes)  # создаём переменную для того что бы увидеть изменился ли размер списка(были ли удалены некоторые элементы)
            for i in range(0, len(notes)):  # перебираем список заметок
                for j, k in notes[i].items():
                    if j == 'Имя' and k == user_choose:  # если нужная нам заметка найдена добавляем её индекс в нужный для этого список note_to_delete
                        note_to_delete.append(i)
                    elif j == 'Заголовок' and k == user_choose:
                        note_to_delete.append(i)
            for i in note_to_delete:
                notes.remove(notes[i])  # удаляем те заметки чьи индексы мы занесли в список note_to_delete
            if before_delite == len(notes):
                print("Заметок с таким именем пользователя или заголовком не найдено")  # если размер списка не изменился, то сообщаем что такой заметки нет
            else:
                print('Успешно удалено. Остались следующие заметки:')  # раз размер списка изменился то и удаление прошло успешно, сообщаем об этом пользователю
                display_notes(notes)  # выводим оставшиеся заметки
            continue
        elif user_answer == 'нет':  # выходим из цикла
            break
        else:  # если ввод неверный повторяем запрос
            print("Неверный ввод")
            continue

note_list = [] #создаём список
print('Добро пожаловать в менеджер заметок!')
while True:
    print('\nМеню действий: \n1. Создать новую заметку\n2. Показать все заметки\n3. Обновить заметку\n4. Удалить заметку\n5. Найти заметки\n6. Выйти из программы')
    user_commande = input('Ваш выбор(введите номер команды): ')

    if user_commande == '1':
        note_list.append(create_note())
        continue
    elif user_commande == '2':
        display_notes(note_list)
        continue
    elif user_commande == '3':
        if note_list != []:
            print('Выберите какую заметку редактировать')
            display_notes(note_list)
            while True:
                user_choice = input('Ваш выбор: ')
                try:
                    note_to_update = convert(user_choice)
                    if note_to_update - 1 > len(note_list):
                        print('Заметки с таким номером нет')
                        continue
                    else:
                        update_note(note_list[note_to_update - 1])
                        break
                except ValueError as e:
                    print(e)
        else:
            print('заметок нет')
        continue

    elif user_commande == '4':
        if note_list != []:
            delete_note(note_list)
            continue
        else:
            display_notes(note_list)
            continue

    elif user_commande == '5':
        user_keyword_choice = input('Введите ключевое слово (или оставьте пустым для продолжения):')
        user_status_choice = input('Введите статус заметки (или оставьте пустым для продолжения):')
        if user_keyword_choice == '' and user_status_choice == '':
            print('поиск не совершился')
        elif user_keyword_choice == '' and user_status_choice != '':
            print('поиск по статусу')
            search_notes(note_list, status=user_status_choice)
        elif user_keyword_choice != '' and user_status_choice == '':
            print('поиск по ключевому слову')
            search_notes(note_list, user_keyword_choice)
        else:
            print('поиск по ключевому слову и статусу')
            search_notes(note_list, user_keyword_choice, user_status_choice)
    elif user_commande == '6':
        break
    else:  # если ввод неверный повторяем запрос
        print("Неверный выбор. Пожалуйста, выберите действие из списка.")
        continue