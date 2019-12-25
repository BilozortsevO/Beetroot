def square(start, stop):
    if start.isdigit() and stop.isdigit():
        start, stop = int (start), int (stop)
        if start > stop:
            for i in range (start-1, stop-1, -1):
                yield i**2
        else:
            for i in range (start, stop):
                yield i**2
    else :
        print ('Please insert integer digits.')
    
user_sq = square (input ('Please insert start number of range: '),
                  input ('Please inster stop nimber of range: '))
for i in user_sq:
    print (i, end = ' ')
