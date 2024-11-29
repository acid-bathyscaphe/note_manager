note_dictionary = {'username' : input("Введите имя пользователя: "), 'titles' : ['none'], 'content' : input("Введите описание заметки: "), 'status': input("Введите статус заметки: "), 'created_date': input("Введите дату создания заметки в формате день.месяц.год, например 10.11.2024: "), 'issue_date': input("Введите дату истечения заметки (дедлайн) в формате день.месяц.год, например 10.12.2024: ")}
title1 = input("Введите 1-ый заголовок заметки: ")
title2 = input("Введите 2-ой заголовок заметки: ")
title3 = input("Введите 3-ий заголовок заметки: ")
note_dictionary['titles'] = [title1, title2, title3]
print(note_dictionary['username'])
print(note_dictionary['titles'])
print(note_dictionary['content'])
print(note_dictionary['status'])
print(note_dictionary['created_date'][:5])
print(note_dictionary['issue_date'][:5])
