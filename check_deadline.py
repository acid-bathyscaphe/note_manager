import datetime
current_date = datetime.date.today() #получаем текущую дату и заносим её в переменную
print(f"Текущая дата: {current_date}")

def parse_issue_date(user_input): #функция которая переводит ввод пользователя в
    try:
        return datetime.datetime.strptime(user_input, '%d-%m-%Y').date()
    except ValueError:
        raise ValueError(
            "Некорректный формат даты. Убедитесь, что вводите дату в формате день-месяц-год (например, 10-12-2024).")

while True: #создаём цикл который будет получать дату дедлайна от пользователя, и если ввод неверный выводить сообщение и повторять запрос
    user_input = input("Введите дату дедлайна (в формате день-месяц-год): ")
    try:
        issue_date = parse_issue_date(user_input)
        break
    except ValueError as e:
        print(e)

if issue_date < current_date: #сравниваем дату дедлайна с текущей датой и выводим сообщение в зависимости от полученного результата
        days_overdue = (current_date - issue_date).days
        print(f"Внимание! Дедлайн истёк {days_overdue} дня(ей) назад.")
elif issue_date == current_date:
        print("Дедлайн сегодня!")
else:
        days_left = (issue_date - current_date).days
        print(f"До дедлайна осталось {days_left} дня(ей).")







