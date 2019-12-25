def factorial(n):
    l = []
    for i in range (1, n):
        if i == 1:
            return 1
        return l.append (n * factorial (n-1))

print (factorial (5))
