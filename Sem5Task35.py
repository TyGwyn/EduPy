n = int(input("Введите число, которое хотите проверить: "))
def simple(n):
    i = 2
    is_Prime = True
    while i < n and is_Prime:
        if n % i == 0:
            is_Prime = False
        i+=1
    if is_Prime:
        return 'Простое'
    return 'Не является простым'
print(simple(n))


