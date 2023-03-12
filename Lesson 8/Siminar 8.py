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


print(' 1. Открыть файл\n 2. Сохранить файл\n 3. Показать все контакты\n 4. Создать контакт\n 5. Изменить контакт\n 6. Найти контакт\n 7. Удалить контакт\n 8. Выход')

# path = 'file.txt'

# def open_file(path):  
#         with open(path, 'r', encoding='UTF-8') as file:
#             data = file.readlines()
#             for contact in data:
#                 print(contact.split(';'))
# number = input('введите пункт меню: ')
# while True:
#     match number:
#         case 1:
#             open_file(path)
#         case 2:
#             pass
#         case 3:
#             pass

phone_book = []
path = 'file.txt'

def open_file(path):
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
        for contact in data:
            cont = []
            for field in contact.split(';'):
                cont.append(field.strip())
            phone_book.append(cont)


def show_contacts(phone_book):
    for i, contact in enumerate(phone_book, 1):
        print(f'{i}. {contact[0]:<20} {contact[1]:<10} {contact[2]:<5}')

def add_contact():
    name = input('Введите имя и фамилию: ')
    phone = input('Введите телефон: ')
    comment = input('Введите комментарий: ')
    phone_book.append(list([name, phone, comment]))

def search_contact(phone_book):
    search = input('Введите ключевой элемент: ')
    for contact in phone_book:
        for field in contact:
            if search in field:
                print(contact)

def change_contact(phone_book):
    count = 0
    search = input('Введите ключевой элемент контакта который хотите изменить: ')
    for contact in phone_book:
        for field in contact:
            if search in field:
                print(contact)
                print(count)
                print('Этот контакт выхотели поменять ?')
                choose = int(input('если да то введите 1, если нет то 0):'))
                if choose == 1:
                    name = input('Введите имя и фамилию: ')
                    phone = input('Введите телефон: ')
                    comment = input('Введите комментарий: ')
                    print(phone_book[count])
                    phone_book[count] = list([name, phone, comment])
                    return print(phone_book[count])
        count += 1
                
def delete_contact(phone_book):
    with open(path, 'w', encoding='UTF-8') as file:
        count = 0
        search = input('Введите ключевой элемент контакта который хотите удалить: ')
        for contact in phone_book:
            for field in contact:
                if search in field:
                    print(contact)
                    print('Этот контакт выхотели поменять ?')
                    choose = int(input('если да то введите 1, если нет то 0):'))
                    if choose == 1:
                        phone_book.remove(contact)
                        path.write(phone_book)
                        return show_contacts(phone_book)
            count += 1
        

while True:
    number = int(input('Введите пункт меню: '))
    match number:
        case 1:
            open_file(path)
            print('Файл успешно загружен')
        case 2:
            pass
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

