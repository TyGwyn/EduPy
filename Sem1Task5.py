i = int(input("Введите вагон по счёту: "))
j = int(input("Введите номер на вагоне: "))

if i == j:
    print("Невозможно узнать")
else:
    print(i + j - 1)