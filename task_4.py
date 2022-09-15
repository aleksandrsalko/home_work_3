# Напишите программу, которая будет преобразовывать десятичное число в двоичное. 
# Подумайте, как это можно решить с помощью рекурсии.

# Пример:
#     45 -> 101101
#     3 -> 11
#     2 -> 10

def dec_bin (num_dec, num_bin = '') :
  if num_dec != 0 :
    num_bin += dec_bin (num_dec // 2, num_bin) + str (num_dec % 2)
  return num_bin
  
num_dec = int (input ('Введите десятичное число: '))
num_bin = dec_bin (num_dec)
print (num_bin)
  


