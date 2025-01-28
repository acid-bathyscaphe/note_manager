def handle_error(error_type):

    if error_type == "invalid_input":
        print("❌ Ошибка: Введены некорректные данные. Попробуйте снова.")
    elif error_type == "note_not_found":
        print("⚠️ Ошибка: Заметка не найдена. Проверьте правильность ввода.")
    elif error_type == "empty_list":
        print("📭 Список заметок пуст. Добавьте новую заметку.")
    else:
        print("⚠️ Неизвестная ошибка. Обратитесь в службу поддержки.")