from color_output import display_notes_with_colors
from error_handling_ui import handle_error

def display_page(notes, page, notes_per_page=3):
    start = (page - 1) * notes_per_page
    end = start + notes_per_page
    page_notes = notes[start:end]

    print(f"\n=== Страница {page} ===")
    for note in page_notes:
        display_notes_with_colors(note)
    print("\n[N] Следующая страница | [P] Предыдущая страница | [Q] Выход")

def paginate_notes(notes):
    page = 1
    notes_per_page = 3
    total_pages = (len(notes) + notes_per_page - 1) // notes_per_page

    while True:
        display_page(notes, page, notes_per_page)
        choice = input("Ваш выбор: ").strip().lower()

        if choice == "n" and page < total_pages:
            page += 1
        elif choice == "p" and page > 1:
            page -= 1
        elif choice == "q":
            print("Выход из навигации.")
            break
        else:
            handle_error("invalid_input")