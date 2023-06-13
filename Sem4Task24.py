n = int(input("Cколько кустов растёт на грядке: "))
mas = list()
for i in range(n):
    a =int(input('Введите количество ягод на кусте: '))
    mas.append(a)

max_count = list()
for i in range(len(mas)):
       max_count.append(mas[i-2] + mas[i-1] + mas[i])
print(max(max_count))