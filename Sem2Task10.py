n = int(input("Введите количество монет: "))
count_zero = 0
count_one = 0
for i in range(n):
    x = int(input("На монете орёл или решка? Введите числом (орёл - 0, решка - 1): "))
    if x == 0:
        count_zero += 1
    else:
        count_one += 1
    print("Теперь все монеты: ")
    if count_one > count_zero:
        print("На орле", count_zero)
    else:
        print("На решке", count_one)