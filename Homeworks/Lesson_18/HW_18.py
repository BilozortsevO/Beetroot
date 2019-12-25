def factorial (i):
    a = 1
    if i > 0:
        for n in range(2, i+1):
            a *= n
        return a
    else:
        print ('Number shuold be positive integer!')

def main():
    print (factorial (int (input ('Enter Factorial number: '))))

if __name__ == '__main_':
    main()
