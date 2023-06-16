a = int(input("Введите число, которое хотите возвезти в степень: "))
b = int(input("В какую степень вы хотите его возвести? "))
def pow_num(a,b):
    if a == 1 or b == 0:
        return 1
    return a * (pow_num(a,b-1))
print("Результат возведения в степень: ", pow_num(a,b))

