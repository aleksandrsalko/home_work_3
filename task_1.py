# 1- Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def sum_odd_index(lst):
    sum = 0
    nechet = []
    for i in range(len(lst)):
        if i % 2 != 0:
            sum += lst[i]
    print(f"Сумма элементов на нечётных позициях = {sum}")

lst = list(map(int, input("Введите числа через пробел:\n").split()))
sum_odd_index(lst)

