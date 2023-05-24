'''
На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
Выведите минимальное количество монет, которые нужно перевернуть
'''
n = 3

gerb = 0
reshka = 0
flag = True
iter = 1
while(flag):
    moneta = int(input("Введите 0 - если герб, 1 - если решка: "))

    if(moneta == 0):
        gerb += 1
    elif(moneta == 1):
        reshka += 1
    else:
        print("Неверный ввод")
        flag = False

    iter += 1

    if(iter > n):
        flag = False

if(gerb < reshka):
    print(gerb)
else:
    print(reshka)