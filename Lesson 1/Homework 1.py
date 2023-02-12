# Задача 2. Найдите сумму цифр трехзначного числа.

# num = int(input('Please enter three digit number: '))
# print(num %10 + num // 10 %10 + num // 100 %10)



# Задача 4. Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, 
# если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# AllCranes = 60
# Allcranes = AllCranes // 2
# Peter = Allcranes // 3
# Kate = Peter * 2 * 2
# print(f'Kate did cranes: {Kate}, Peter did cranes: {Peter}, Seryozha did cranes:  {Peter}')

# Можно было добавить ещё одну перменную,
# двумя вариантами, Seryozha = AllCranes // 3  или   Seryozha = Peter   
# но я решил сократить код.



# Задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.
# 385916 123456

# Ticket = int(input('Please enter number of ticket: '))
# FirstPart = Ticket // 1000
# FirstPart = FirstPart //100 + FirstPart //10 %10 + FirstPart %10

# SecondPart = Ticket %1000
# SecondPart = SecondPart //100 + SecondPart //10 %10 + SecondPart %10

# if FirstPart == SecondPart:
#     print("I'am so lucky ! ! ! ")
# else:
#     print("I'am unlucky ! (")



# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).

# Можно без ввода данных в консоль ниже сразу переменные с заданными значениями
# Size1 = 3
# Size2 = 2
# Slices = 6


# print('Is it possible to break off slices from a chocolate bar with one break?')
# Size1 = int(input('How many slices long: '))
# Size2 = int(input('How many slices wide: '))
# Slices = int(input('How many slices do you want to break off: '))

# Size = Size1 * Size2
# Remainder = Size - Slices
# if Size1 == 1 or Size2 == 1:
#     print('Yes0')
# else:
#     if Size == Slices:
#         print('Yes1')
#     else:
#         if Remainder == Size1 or Remainder == Size2:
#             print('Yes2')   
#         elif Size1 == Slices or Size2 == Slices:
#             print('Yes3')
#         elif Remainder == Slices and Remainder == Slices:
#             print('Yes4')
#         else:
#             print('No')
