"""
Задача 16: Требуется вычислить, сколько раз встречается некоторое число
 X в массиве A[1..N]. 
 Пользователь в первой строке вводит натуральное число 
 N – количество элементов в массиве. 
 В последующих  строках записаны N целых чисел Ai.
  Последняя строка содержит число X
"""

# list_0 = []
# n = int(input('Input range list: '))
# for i in range(n):
#     list_0.append(int(input()))
# print(list_0)
# x = int(input('Input number X: '))
# count = 0
# for i in range(len(list_0)):
#     if x == list_0[i]:
#         count += 1
# print(f'{x}, meets {count} times !')


"""
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине 
элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное 
число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. 
Последняя строка содержит число X
"""


# # # list_0 = [1, 2, 3, 4, 5]
# list_0 = []
# n = int(input('Input range list: '))
# for i in range(n):
#     list_0.append(int(input()))
# print(list_0)
# x = int(input('Input number: '))


# # ## ! ! ! Финальная версия ! ! !

# # # list_0 = [1, 3, -2, 4, 5]
# print(list_0)
# # # x = 7
# c1 = []
# for i in range(len(list_0)):
#   if x != list_0[i]:
#     c1.append(x - list_0[i])
#     # #print(f'список{c1}')
#   else:
#     break
# if list_0[i] != x or x > len(list_0):
#   a = 1
#   for j in range(len(list_0)):
#     if list_0[j] > list_0[a]:
#       a = j
#       # # print(f'Q {list_0[a]}')
#   print(f'a {list_0[a]}')
# else:
#   print(f'i {list_0[i]}')


"""
*Задача 20: * В настольной игре Скрабл (Scrabble) 
каждая буква имеет определенную ценность. В случае с английским алфавитом 
очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко;
D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка;
K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. 
А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко;
Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка;
Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков.
Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
Будем считать, что на вход подается только одно слово, 
которое содержит либо только английские, либо только русские буквы.
"""


list_0 = {1 : 'AEIOULNSTRАВЕИНОРСТ', 2 : 'DGДКЛМПУ', 3 : 'BCMPБГЁЬЯ', 4 : 'FHVWYЙЫ', 5 : 'KЖЗХЦЧ', 8 : 'JXШЭЮ', 10 : 'QZФЩЪ'}
a = input('Input one word: ').upper()
count = 0
for i in a:
  for j in list_0:
    if i in list_0[j]:
      count += j
print(count)

