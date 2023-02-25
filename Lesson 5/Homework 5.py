"""
Задача 26:  Напишите программу, которая на вход принимает 
два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

*Пример:*

A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8 
"""

# a = int(input('Input number A: '))
# b = int(input('Input number B to exponentiate: '))

# def exponentiation(a, b):
#     if b == 1:
#         return a
#     return exponentiation(a, b -1) * a
        
# print(f'A to degree A = {exponentiation(a, b)}')


"""
Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

*Пример:*

2 2
    4 
"""

# print('Input two numbers to add them')
# a = int(input('Input number A: '))
# b = int(input('Input number B: '))

# def summa(a,b):
#     if b == 0:
#         return a
#     a = a + 1
#     return summa(a, b -1)

# print(f'A and B sum =  {summa(a, b)}')