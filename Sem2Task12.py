x = int(input("Введите сумму искомых чисел: "))
y = int(input("Введите произведение искомых чисел: "))
for i in range(x):
    for j in range(y):
        if x == i + j and y == i * j:
            print("Искомые числа: ",i, "и", j)