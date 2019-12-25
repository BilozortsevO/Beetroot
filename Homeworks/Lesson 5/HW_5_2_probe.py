# Extracting numbers
# Creating a list with the range from 1 to 100

list_ = list (range (1, 101))

# Creating a list with integers from the list
# that are divisible by 7 but not a multiple of 5
result = []
for x in list_ :
    if x % 7 == 0 and x % 5 != 0 :
        result.append(x)
        

print (result)
