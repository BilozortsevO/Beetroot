# Return завершает цикл после 1й итерации и возвращает результат
def make_operation(*args):

    summ = 0
    substr = 0
    multipl = 1
    args = list (args)
    for i in range(1, len(args)+1):
        if args [0] == '+':
            #summ = summ + args[i]
            #print (summ)
            return summ + args[i]
        elif args [0] == '-':
            #substr = args[i]-substr
            #print (substr)
            return args[i]-substr
        elif args [0] == '*':
            #multipl = multipl * args[i]
            #print (multipl)
            return multipl * args[i]
        
        
    

print (make_operation ('+',7,8,15))
print (make_operation ('-',7,8,15))
print (make_operation ('*',7,8,15))
