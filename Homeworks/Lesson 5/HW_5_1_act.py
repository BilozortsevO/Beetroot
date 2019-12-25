# Exclusive common numbers
import random

#Generating of 2 lists of length 10 with random integers from 1 to 10

list1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
list1_rand = [random.randint(1,10) * 1 for list1_rand in list1]

list2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
list2_rand = [random.randint(1,10) * 1 for list2_rand in list2]

print ('List 1: ', sorted(list1_rand))
print ('List 2: ', sorted(list2_rand))

#Cahanging types from list to set to compare the lists content

set1_comp = set (list1_rand)
set2_comp = set (list2_rand)

# Comparing the list1 and list2 content

set3_comp_result = set1_comp.intersection (set2_comp)

# Creating a list with intersection numbers from list1 and list2

list3_comp_result = sorted (list (set3_comp_result))

print (list3_comp_result)
