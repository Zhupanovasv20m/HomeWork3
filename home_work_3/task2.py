# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5
import random

n = int(input('Введите число элементов в массиве: '))
my_list = [random.randint(0, 100) for i in range(n)]
print(my_list)
find_num = int(input('Введите искомое число: '))
count = 1

close_num =[abs(my_list[i]-find_num) for i in range(len(my_list))]
print(my_list[close_num.index(min(close_num))])