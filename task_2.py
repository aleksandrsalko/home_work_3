# 2-Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
#    [2, 3, 4, 5, 6] => [12, 15, 16];
#    [2, 3, 5, 6] => [12, 15]

def prod_pairs(lst):
    l = len(lst)//2 + 1 if len(lst) % 2 != 0 else len(lst)//2
    prod_lst = [lst[i]*lst[len(lst)-i-1] for i in range(l)]
    print(prod_lst)


lst = list(map(int, input("Введите числа через пробел:\n").split()))
prod_pairs(lst)