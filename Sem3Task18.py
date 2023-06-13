n = int(input("Введите количество элементов массива: "))
arr = []
k = 0
for i in range (0, n):
    if k < n:
        k += 1
    arr.append(k)
print (arr)
x = int(input("Введите искомый элемент: "))
res = []
for i in range(n):
    if arr[i] == (x-1):
        res.append(arr[i])
    if arr[i] == (x+1):
        res.append(arr[i])
print (res)