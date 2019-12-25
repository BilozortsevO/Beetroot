# Extracting numbers
# Creating a list with the range from 1 to 100

list_ = list (range (1, 101))

# Finding integers that are divisible by 7

list_7 = list_ [6::7]
print (list_7)
# Finding integers from that are divisible by 7 but not a multiple of 5 and

list_7_5 = list_7 [4::5]
print (list_7_5)
# Changing list type to set to use a difference method

list_7 = set (list_7)
list_7_5 = set(list_7_5)

result = sorted (list_7.difference(list_7_5))
print (result)
