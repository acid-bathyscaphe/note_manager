from os import write

notes = [
    {'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю', 'status': 'новая', 'created_date': '27-11-2024', 'issue_date': '30-11-2024'},
    {'username': 'Мария', 'title': 'Учеба', 'content': 'Подготовиться к экзамену', 'status': 'в процессе', 'created_date': '25-11-2024', 'issue_date': '01-12-2024'},
    {'username': 'Иван', 'title': 'План работы', 'content': 'Завершить проект', 'status': 'выполнено', 'created_date': '20-11-2024', 'issue_date': '26-11-2024'}
]
def display_notes(note_list): #функция которая выводит всё содержимое списка заметок
    print('Список заметок:')
    print('-' * 15)
    if note_list == []:
        print("Заметок нет")
    else:
        for i in range(0, len(note_list)):
            print(i + 1)
            for j, k in note_list[i].items():
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



user_keyword_choice = input('Введите ключевое слово (или оставьте пустым для продолжения):')
user_status_choice = input('Введите статус заметки (или оставьте пустым для продолжения):')
if user_keyword_choice == '' and user_status_choice == '':
    print('поиск не совершился')
elif user_keyword_choice == '' and user_status_choice != '':
    print('поиск по статусу')
    search_notes(notes, status = user_status_choice)
elif user_keyword_choice != '' and user_status_choice == '':
    print('поиск по ключевому слову')
    search_notes(notes, user_keyword_choice)
else:
    print('поиск по ключевому слову и статусу')
    search_notes(notes, user_keyword_choice, user_status_choice)