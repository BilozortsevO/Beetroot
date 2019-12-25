def binar(n):
    n = str(n)
    if not n:
        return 0
    if n[-1] not in '01':
        raise ValueError
    return binar(n[:-1]) * 2 + (n[-1]=='1')

print (binar (int(input('Число: '))))
