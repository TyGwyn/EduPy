n = int(input("Сколько чисел вы хотите поменять местами? "))
def print_reverse(n):
    if n == 0:
        return ''
    k = int(input("Введите последовательность чисел, которые нужно поменять местами: "))
    return print_reverse(n-1) + ' ' + str(k)
print(print_reverse(n))

