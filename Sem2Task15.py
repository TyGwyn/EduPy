##watermelons = [5, 4, 15, 6, 5, 9, 7, 16]
n = int(input("Введите кол-во арбузов: "))
max_weight = 0
min_weight = 1

for i in range(n):
    watermelons = int(input("Введите вес арбуза: "))
    if watermelons > max_weight:
        max_weight = watermelons
    if watermelons < min_weight:
        min_weight = watermelons
print (min_weight)
print (max_weight)