from colorama import Fore, Style

def display_notes_with_colors(note):
        if note['status'].lower() == 'важная':
            print(Fore.RED + f'• Имя пользователя: {note["username"]}\n'
                  f'\tЗаголовок: {note["title"]}\n'
                  f'\tОписание: {note["content"]}\n'
                  f'\tСтатус: {note["status"]}\n'
                  f'\tДата создания: {note["created_date"]}\n'
                  f'\tДедлайн: {note["issue_date"]}\n'
                  f'----------------------------' + Style.RESET_ALL)
        elif note['status'].lower() == 'выполненная' or note['status'].lower() == 'готово':
            print(Fore.GREEN + f'• Имя пользователя: {note["username"]}\n'
                             f'\tЗаголовок: {note["title"]}\n'
                             f'\tОписание: {note["content"]}\n'
                             f'\tСтатус: {note["status"]}\n'
                             f'\tДата создания: {note["created_date"]}\n'
                             f'\tДедлайн: {note["issue_date"]}\n'
                             f'----------------------------' + Style.RESET_ALL)
        elif note['status'].lower() == 'в процессе':
            print(Fore.YELLOW + f'• Имя пользователя: {note["username"]}\n'
                             f'\tЗаголовок: {note["title"]}\n'
                             f'\tОписание: {note["content"]}\n'
                             f'\tСтатус: {note["status"]}\n'
                             f'\tДата создания: {note["created_date"]}\n'
                             f'\tДедлайн: {note["issue_date"]}\n'
                             f'----------------------------' + Style.RESET_ALL)
        else:
            print(Fore.BLUE + f'• Имя пользователя: {note["username"]}\n'
                             f'\tЗаголовок: {note["title"]}\n'
                             f'\tОписание: {note["content"]}\n'
                             f'\tСтатус: {note["status"]}\n'
                             f'\tДата создания: {note["created_date"]}\n'
                             f'\tДедлайн: {note["issue_date"]}\n'
                             f'----------------------------' + Style.RESET_ALL)