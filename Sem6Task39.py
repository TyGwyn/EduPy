mass_1 = []
mass_2 = []
n = int(input("Введите количество элементов 1-го массива: "))
m = int(input("Введите количество элементов 2-го массива: "))
count_1 = 0
count_2 = 0
while count_1 < n:
    a = int(input("Введите элемент 1-го массива: "))
    mass_1.append(a)
    count_1 += 1
print(mass_1)
while count_2 < m:
    b = int(input("Введите элемент 2-го массива: "))
    mass_2.append(b)
    count_2 += 1
print(mass_2)
mass_1 = set (mass_1)
mass_2 = set (mass_2)
res_mass = {}
res_mass = sorted(mass_1.difference(mass_2))
print (res_mass)