
def make_operation_plus_minus(*args):
    res = 0
    args = list (args)
    
    for i in range(1, len(args)):
        
        if args [0] == '+':
            res += args[i]            
    
        elif args [0] == '-':
            res = args[i] - res
            
    return res

def make_operation_multiply(*args):
    res = 1
    args = list (args)
    
    for i in range(1, len(args)):
        
        if args [0] == '*':
            res *= args[i]
            
    return res
        
        
    

print (make_operation_plus_minus ('+',7,8,15))
print (make_operation_plus_minus ('-',5,7,12))
print (make_operation_multiply ('*',2,3,6))
