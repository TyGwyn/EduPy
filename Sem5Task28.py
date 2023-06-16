a = int(input("Введите 1-ое число: "))
b = int(input("Введите 2-ое число: "))
def get_sum(a,b):
    if b == 0:
        return a
    return get_sum(a+1,b-1)
print("Сумма чисел равна: ", get_sum(a,b))