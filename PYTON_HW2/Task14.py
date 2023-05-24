'''
Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
'''

n = 8
result = 1
count = 1

if(n <= 1):
    print("Неверное значение.")
else:
    while(result*2 <= n):
        print(count)
        result *= 2
        count += 1