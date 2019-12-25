def fib_recursive(n):
    if n ==0 or n ==1:
        return n
    s = fib_recursive(n-1)+fib_recursive(n-2)
    return s

def lists (i):
    l = []
    for k in range (i+1):
        l.append (fib_recursive(k))
    return l

print (lists(int(input ('Номер числа Фибоначчи: '))))
