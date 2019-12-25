s = ''

def binar(n):
    global s
    if n == 0:
        return
    binar (n//2)
    s = s + str(n % 2)

binar (int (input ('Введите десяточное целое число: ')))
print (s)
