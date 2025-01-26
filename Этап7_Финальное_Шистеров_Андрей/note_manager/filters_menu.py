from error_handling_ui import handle_error

def filter_notes(notes, filter_type, filter_value):
    if filter_type == "keyword":
        return [note for note in notes if filter_value.lower() in note['title'].lower()]
    elif filter_type == "status":
        return [note for note in notes if note['status'] == filter_value]
    elif filter_type == "date":
        return [note for note in notes if note['date'] == filter_value]
    else:
        return notes

def filters_menu(notes):
    while True:
        print("\n=== Фильтры ===\n"
            "1. По ключевому слову\n"
            "2. По статусу (Важная, Выполненная, Новая)\n"
            "3. По дате\n")
        choice = input("Выберите фильтр: ")

        if choice == "1":
            keyword = input("Введите ключевое слово: ")
            filtered_notes = filter_notes(notes, "keyword", keyword)
        elif choice == "2":
            status = input("Введите статус (Важная/Выполненная/Новая): ")
            filtered_notes = filter_notes(notes, "status", status)
        elif choice == "3":
            date = input("Введите дату (формат: ГГГГ-ММ-ДД): ")
            filtered_notes = filter_notes(notes, "date", date)
        else:
            handle_error("invalid_input")
            continue
        if filtered_notes:
            return filtered_notes
        else:
            print("Нет заметок, соответствующих фильтру.")
            return

