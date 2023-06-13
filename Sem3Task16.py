n = int(input("Введите количество элементов массива: "))
arr = []
k = 0
for i in range (0, n):
    if k < n:
        k += 1
    arr.append(k)
print (arr)
x = int(input("Введите искомый элемент: "))
count = 0
for i in range(n):
    if arr[i] == (x):
        count += 1
print ("Искомый элемент встречается: ", count)