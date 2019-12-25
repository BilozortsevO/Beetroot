
def square(start, stop):
    squares = []
    if start.isdigit() or stop.isdigit():
        if int (start) > int (stop):
            for i in range (int (start), int(stop), -1):
                yield squares.append (i**2)
        else:
            for i in range (int (start), int(stop)):
                yield i**2
    else :
        print ('Please insert integer digits.')
    
print (square (start = input ('Please insert start number of range: '),
               stop = input ('Please inster stop nimber of range: ')))
