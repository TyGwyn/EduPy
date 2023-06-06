##day_num = int(input("Введите количество дней наблюдения: "))
temp = [-20, 30, 50, 35, -40, 50, 10, -10]
schet = 0
max = 0
for i in (temp):
    if i > 0:
        schet += 1
        print ("Счёт дней равен:", schet)
    else:
        if schet > max:
            max = schet
            print ("Максимум равен: ", max)
        schet = 0
print("Максимальное количество дней:", max)