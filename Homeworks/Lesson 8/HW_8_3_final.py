
def make_operation_plus_minus(*args):
    ops = '+-*/'
    op = args[0]
    digits = args[1:]
    if op not in ops:
        print ('Operator should be chosed from', ops)
        return
    
    for i in range(1, len(args)):
        
        if type(args[i]) is not int:
            print ('Only digits should be in input')
            return
        
        if args [0] == '+':
            res = digits [0]
            for x in digits [1:]:
                res += x
            return res
        if args [0] == '-':
            res = digits [0]
            for x in digits [1:]:
                res -= x
            return res
        if args [0] == '*':
            res = digits [0]
            for x in digits [1:]:
                res *= x
            return res
        if args [0] == '/':
            res = digits [0]
            for x in digits [1:]:
                res /= x
            return res
       

print (make_operation_plus_minus ('+',7,8,15))
print (make_operation_plus_minus ('-',5,7,12))
print (make_operation_plus_minus ('*',2,3,6))
print (make_operation_plus_minus ('/',123,2,3))
