a = int(input("Введите число A: "))
fib_prev = 0
fib_curr = 1
n = 2
while fib_curr < a:
    fib_next = fib_prev + fib_curr
    fib_prev = fib_curr
    fib_curr = fib_next
    n += 1
if fib_curr == a:
    print ("Число", a, "является", n,"-ым числом Фибоначчи")
else:
    print ("Число", a, "не является числом Фибоначчи, результат равен -1")