import datetime

note_list = [] #создаём список
print('Добро пожаловать в менеджер заметок! Вы можете добавить новую заметку.')
current_date = datetime.date.today().strftime('%d-%m-%Y') #получаем текущую дату и заносим её в переменную

def parse_issue_date(user_input): #функция которая переводит ввод пользователя в datetime
    try:
        return datetime.datetime.strptime(user_input, '%d-%m-%Y').date()
    except ValueError:
        raise ValueError(
            "Некорректный формат даты. Убедитесь, что вводите дату в формате день-месяц-год (например, 10-12-2024).")

def create_note():  # функция которая добавляет в список заметку ввиде словаря

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

is_the_first_note = True #создаём переменную которая отслеживает создание первой заметки
while True:
    if is_the_first_note: #создаём первую заметку
        note_list.append(create_note())
        is_the_first_note = False
        continue
    user_answer = input('Хотите добавить ещё одну заметку? (да/нет): ') #спрашиваем пользователя о создании ещё одной заметки
    if user_answer == 'да': #создаём ещё одну заметку и повторяем запрос
        note_list.append(create_note())
        continue
    elif user_answer == 'нет':#выходим из цикла
        display_notes(note_list)
        break
    else: #если ввод неверный повторяем запрос
        print("Неверный ввод")
        continue