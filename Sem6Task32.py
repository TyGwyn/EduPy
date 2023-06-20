mas = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
res_mas = []
min_num = int(input("Введите минимальное значение диапозона: "))
max_num = int(input("Введите максимальное значение диапозона: "))
for i in range (len(mas)):
    if min_num<=mas[i]<=max_num:
        print (i)
        res_mas.append(mas[i])
        print(res_mas)