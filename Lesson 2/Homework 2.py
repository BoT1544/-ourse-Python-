# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

# coin = int(input('Please input How many coins will: '))
# zero = 0
# one = 0
# count = 0
# while count < coin:
#     side = int(input('Input side, eagle is 1, tails is 0: '))
#     if side == 0:
#         zero += 1
#     else:
#         one += 1
#     count += 1
# if zero < one:
#     print(f'fewer coins tails {zero}')
# else:
#     print(f'fewer coins eagle {one}')



# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.


# print('input two numbers X and Y <= 1000.')
# x = int(input('Input number X: '))
# y = int(input('Input number Y: '))
"""
import random
x = random.randint(1,1000)
y = random.randint(1,1000)
"""
# s = x + y
# print(f'Sum of numbers is {s}')
# p = x * y
# print(f'Works of numbers is {p}')
# temp = s
# for i in range(s):
#     temp -= 1
#     temp1 = s - temp
#     temp2 = temp * temp1
#     if temp2 == p:
#         print(f'x = {temp}, Y = {temp1}')
#         break


# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

# n = int(input('Input number: '))
# for i in range(n):
#     a = 2 ** i
#     if a < n:
#         print(a)