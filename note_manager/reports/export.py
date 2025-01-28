import json

def export_notes_to_file(notes, filename, format='txt'):
    if format == 'txt':
        with open(filename, 'w', encoding='utf-8') as file:
            for i, note in enumerate(notes, start=1):
                file.write(f'Имя пользователя: {note["username"]}\n'
                        f'Заголовок: {note["title"]}\n'
                        f'Описание: {note["content"]}\n'
                        f'Статус: {note["status"]}\n'
                        f'Дата создания: {note["created_date"]}\n'
                        f'Дедлайн: {note["issue_date"]}\n'
                        f'----------------------------\n')
    if format == 'json':
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(notes, file, indent=4, ensure_ascii=False)
