def change_status(status): #создаём функцию которая будет получать или изменять статус заметки
    while True:
        status_number = input('1 - "выполнено",2 - "в процессе" или 3 - "отложено": ')
        status = ''
        if status_number == '1':
            status = "выполнено"
        elif  status_number == '2':
            status = "в процессе"
        elif  status_number == '3':
            status = "отложено"
        else:
            print("Неверный ввод") #проверка ввода на ошибки
            continue
        break
    return status
print('Введите число соответсвующее текущему статусу заметки ')
status = ''
status = change_status(status) #вызываем функцию и сохраняем результат в переменную

print('текущий статус заметки:', status)
while True:
    user_choose = input('Хотите изменить статус заметки? 1 - да, 2 - нет(выйти из программы): ') #даём пользователю выбор изменять ли статус
    if user_choose == '1':
        while True:
            print('Введите число соответсвующее статусу заметки на который вы хотите его изменить')
            status = change_status(status) #если пользователь решил изменить статус - повторно вызываем функцию и сохраняем результат
            print('изменённый статус заметки:', status) #выводим изменённый статус и завершаем работу цикла
            break

    elif user_choose == '2': #если пользователь решил не менять статус - выходим из цикла
        break
    else:
        print("Неверный ввод") #ещё одна проверка ввода на ошибки
        continue