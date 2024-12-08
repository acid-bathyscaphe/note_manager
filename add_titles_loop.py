title_list = [] #создаём список
while True:
    title_list.append(input("Введите заголовок заметки(или оставьте пустым для завершения): ")) #добавляем заголовок в список
    if title_list[len(title_list)-1] == '':
        title_list.remove(title_list[len(title_list)-1]) #если введён пустой заголовок, то убираем его из списка и заканчиваем цикл
        break
print('Заголовки заметки: ')
for i in range(0, len(title_list)):
    print('-', title_list[i]) #выводим результат на экран

