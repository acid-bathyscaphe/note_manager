import datetime

print('Добро пожаловать в менеджер заметок! Вы можете добавить новую заметку.')
current_date = datetime.date.today().strftime('%d-%m-%Y')

def create_note(): # функция которая добавляет в список заметку ввиде словаря
     return ({'Имя': input("Введите имя пользователя: "), 'Заголовок': input("Введите заголовок заметки: "),
                      'Описание': input("Введите описание заметки: "), 'Статус': input("Введите статус заметки: "),
                      'Дата создания': current_date,
                      'Дедлайн': input(
                          "Введите дату истечения заметки (дедлайн) в формате день.месяц.год, например 10.12.2024: ")})


for j, k in create_note().items():
    if j == 'Имя':
        print('Заметка создана:')
    print(j,':',k)
