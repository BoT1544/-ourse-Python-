"""
1. Открыть файл
2. Сохранить файл
3. Показать все контакты
4. Создать контакт
5. Изменить контакт
6. Найти контакт
7. Удалить контакт
8. Выход
"""

"""
Иванов Иван Иванович; +79031233321; Работа
Петров Василий Михалыч; +79031233321; Друг
Васильев Инакентий Петрович; +79295328647; сто
Максимович Евгений Иванович; +79171230965; заказ кухни
"""


def menu():
    print(' 0. Показать Меню\n 1. Открыть файл\n 2. Сохранить файл\n 3. Показать все контакты\n 4. Создать контакт\n 5. Изменить контакт\n 6. Найти контакт\n 7. Удалить контакт\n 8. Выход')

phone_book = []
path = 'file.txt'


def open_file(path):
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
        for contact in data:
            cont = []
            for field in contact.split(';'):
                cont.append(field.strip().title())
            phone_book.append(cont)


def show_contacts(phone_book):
    for i, contact in enumerate(phone_book, 1):
        print(f'{i}. {contact[0]:<20} {contact[1]:<10} {contact[2]:<5}')

def chek_digit():
    phone = input('Введите телефон: ')
    if phone.isdigit():
        if len(phone) == 11:
            if phone[0] == '7':
                phone = list(phone)
                phone.insert(0, '+')
                phone = ''.join(phone)
                return phone
            phone = phone.replace('8', '7', 1)
            phone = list(phone)
            phone.insert(0, '+')
            phone = ''.join(phone)
            return phone
        print('Некоректная длинна номера')
        return chek_digit()
    print('Введите номер только цифрами и без "+"')
    return chek_digit()

def add_contact():
    name = input('Введите имя и фамилию: ').title()
    ###phone = input('Введите телефон: ')
    phone = chek_digit()
    comment = input('Введите комментарий: ').title()
    phone_book.append(list([name, phone, comment]))
    print(f'\nКонтакт: "{name} {phone} {comment}" успешно создан')


def search_contact(phone_book):
    count = 0
    i = 0
    search = input('Введите ключевой элемент: ').title()
    for contact in phone_book:
        for field in contact:
            if search in field:
                i += 1
                print(f'По ключевому элементу "{search}" был найден контакт:\n{i}. {contact[0]} {contact[1]} {contact[2]}\n')
                count += 1
    if count == 0:
        print(f'Совпадений по ключевому элементу "{search}" не найдено')

def change_contact(phone_book):
    count = -1
    count_1 = 0
    search = input('Введите ключевой элемент контакта который хотите изменить: ').title()
    for contact in phone_book:
        count += 1
        for field in contact:
            if search in field:
                print(f'\n"{contact[0]} {contact[1]} {contact[2]}"')
                print('Этот контакт выхотели поменять ?')
                choose = int(input('если да, то введите 1, если нет то 0):'))
                if choose == 1:
                    name = input('Введите имя и фамилию: ').title()
                    ### phone = input('Введите телефон: ')
                    phone = chek_digit()
                    comment = input('Введите комментарий: ').title()
                    count_1 += 1
                    print(f'\nконтакт: "{phone_book[count][0]} {phone_book[count][1]} {phone_book[count][2]}"')
                    phone_book[count] = list([name, phone, comment])
                    return print(f'был изменён на: "{phone_book[count][0]} {phone_book[count][1]} {phone_book[count][2]}"')
    if count_1 == 0:
        print(f'\nСовпадений по ключевому элементу "{search}" не найдено или совпадения закончились\n')
                
def delete_contact(phone_book):
        count = 0
        search = input('Введите ключевой элемент контакта который хотите удалить: ').title()
        for contact in phone_book:
            for field in contact:
                if search in field:
                    print(f'\n"{contact[0]} {contact[1]} {contact[2]}"')
                    print('Этот контакт выхотели поменять ?')
                    choose = int(input('если да то введите 1, если нет то 0):'))
                    if choose == 1:
                        phone_book.remove(contact)
                        print(f'\nКонатк: "{contact[0]} {contact[1]} {contact[2]}" был успешно удалён\nОбнавлёный список контактов:')
                        return show_contacts(phone_book)
            count += 1


def save_contact(phone_book):
    file_to_save = []
    for contact in phone_book:
        str_list = []
        for value in contact:
            str_list.append(value)
        file_to_save.append('; '.join(str_list))
    save_file = '\n'.join(file_to_save)
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(save_file)
    print('Файл успешно сохранён')
    

            
menu()
print('Для начала работы, выбереите пункт меню: "1. Открыть файл"')
while True:
    number = int(input('Введите пункт меню: '))
    match number:
        case 0:
            menu()
        case 1:
            open_file(path)
            print('Файл успешно загружен')
        case 2:
            save_contact(phone_book)
        case 3:
            show_contacts(phone_book)
        case 4:
            add_contact()
        case 5:
            change_contact(phone_book)
        case 6:
            search_contact(phone_book)
        case 7:
            delete_contact(phone_book)
        case 8:
            break
print('Досвидания')

