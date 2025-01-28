from .error_handling_ui import handle_error

def filter_notes(notes, filter_type, filter_value):
    if filter_type == "keyword":
        return [note for note in notes if filter_value.lower() in note['title'].lower()]
    elif filter_type == "status":
        return [note for note in notes if note['status'] == filter_value]
    elif filter_type == "date":
        return [note for note in notes if note['issue_date'] == filter_value or note['created_date'] == filter_value]
    else:
        return notes

def filters_menu(notes):

    def crop(param_for_filter, value):
        filtered_notes = filter_notes(notes, param_for_filter, value)
        if filtered_notes:
            return filtered_notes
        else:
            filtered_notes = []
            return filtered_notes


    while True:
        print("\n=== Фильтры ===\n"
            "1. По ключевому слову\n"
            "2. По статусу (Важная, Выполненная, Новая)\n"
            "3. По дате\n")
        choice = input("Выберите фильтр: ")

        if choice == "1":
            keyword = input("Введите ключевое слово: ")
            filtered_notes = crop("keyword", keyword)
            return filtered_notes

        elif choice == "2":
            status = input("Введите статус (Важная/Выполненная/Новая): ")
            filtered_notes = crop("status", status)
            return filtered_notes
        elif choice == "3":
            date = input("Введите дату (формат: ДД-ММ-ГГГГ): ")
            filtered_notes = crop("date", date)
            return filtered_notes
        else:
            handle_error("invalid_input")
            continue


