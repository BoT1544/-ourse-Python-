# def sum_numbers(n, y = 'hello'): # если не будет второй переменной выведится переменная по умолчанию !
#     print(y)
#     summa = 0
#     for i in range(1,n +1):
#         print(i)
#         summa += i
#     return summa
# print(sum_numbers(5, 'qwert'))

# def sum_str(*abc):
#     res = ' '
#     for i in abc:
#         res += i
#     return res
# print(sum_str('q', 'e', 'l'))
# print(sum_str('q', 'e', 'l', 'r', 'f'))
# print(sum_str('1', '8', '9'))



## 1 способ вызова функций при помощи модулей из другого файла !
# import Modul1
# print(Modul1.max1(5, 9))   

## 2 способ вызова функций при помощи модулей из другого файла !
## тут не нужно каждый раз перед функцией писать названия файла для вызова !
## Но после import нужно перечислять все функции которые будут использоватся,
## что бы не перечеслять их можно просто написать * "import *" !
# from Modul1 import max1
# print(max1(10, 9))

## Переименовать название файла програмным способом, только на время действия программы !
# import Modul1 as m1
# print(m1.max1(11, 9))



# def fib(n):
#     if n in [1, 2]:
#         return 1
#     #print(f'fib+ = {fib(n - 1) + fib(n - 2)}')
#     return fib(n - 1) + fib(n - 2)

# list_1 = []
# for i in range(1, 10):
#     print(f'i{i}')
#     list_1.append(fib(i))
#     print(f'list{list_1}')
# print(list_1)



# def quick_sort(array):
#     if len(array) <= 1:
#         return array
#     else:
#         pivot = array[0]
#     less = [i for i in array[1:] if i <= pivot]
#     greater = [i for i in array[1:] if i > pivot]
#     return quick_sort(less) + [pivot] + quick_sort(greater)

# #print(quick_sort([14,5,9,6,3,58,7,5,2,7]))
# print(quick_sort([10,5,2]))


def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

list1 = [1,5,6,9,8,7,2,1,55,2,4]
merge_sort(list1)
print(list1)
        