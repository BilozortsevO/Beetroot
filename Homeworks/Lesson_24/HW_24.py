class BZeroError (Exception):
    def __init__(self):
        print ('b не может быть равным нулю.')

try:
    a = int(input('Введите число a: '))
    b = int(input('Введите число b: '))
except ValueError:
    print ('Неверно введено число!')
else:
    if b == 0:
        raise BZeroError

print ((a**2)/b)


