def fib_recursive(n):
    if n ==0 or n ==1:
        return n
    s = fib_recursive(n-1)+fib_recursive(n-2)
    print (s, end = "")


fib_recursive(int(input ('Номер числа Фибоначчи: ')))
