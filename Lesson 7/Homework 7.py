"""
 Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
 Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
 Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) 
 в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, 
 если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
 Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, 
 если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
 
 **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
    **Вывод:** Парам пам-пам  
 """

# # text = input("Input text: ").lower()
# text = 'пара-ра-рам рам-пам-папам па-ра-па-да'
# text = text.split()

# letter = ['а', 'я', 'у', 'ю', 'о', 'е', 'ё', 'э', 'и', 'ы']

# x = []
# for i in text:
#     for j in letter:
# #         print(j)
#         if j in i:
# #             print(i.count(j))
#             x.append(i.count(j))
# # print(x)
# if len(x) == x.count(x[0]):
#     print('Парам пам-пам')
# else:
#     print('Пам парам')


"""
Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. 
Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). Примечание: бинарной операцией называется любая операция, 
у которой ровно два аргумента, как, например, у операции умножения.

*Пример:*

**Ввод:** `print_operation_table(lambda x, y: x * y) ` 
**Вывод:**
1 2 3 4 5 6

2 4 6 8 10 12
3 6 9 12 15 18
4 8 12 16 20 24
5 10 15 20 25 30
6 12 18 24 30 36
"""

# Ниже преставлена моя версия написаная до семинара на котором была разобрана домашняя работа,
# скорее всего не совсем отвечаюшая требованиям задания
"""
def operation_table(x, y):
   for i in range(1, x + 1):
      for j in range(1, y +1):
         print(i * j, end = ' ')
      print('\n')

rows = 6
colums = 6

operation_table(rows, colums)
"""


# def print_operation_table(operation, num_rows: int, num_columns: int):
#    for row in range(1, num_rows + 1):
#       for column in range(1, num_columns +1):
#          print(f'{operation(row, column):^5}', end = '')
#       print()

# operation = lambda x, y: x * y

# print_operation_table(operation, num_rows = 6, num_columns = 6)