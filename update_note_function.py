import datetime

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
    note['Дедлайн'] = issue_date #не забываем добавить дедлайн в заметку
    return note


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

note = create_note() #Создаём заметку
note = update_note(note) #Обновляем данные
print(note)