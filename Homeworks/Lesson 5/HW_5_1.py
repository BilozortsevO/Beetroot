# Exclusive common numbers
import random

list1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
list1_rand = [random.randint(1,10) * 1 for list1_rand in list1]
print (sorted(list1_rand))

list2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
list2_rand = [random.randint(1,10) * 1 for list2_rand in list2]
print (sorted(list2_rand))

list3 = sorted(list1_rand) - sorted(list2_rand)
print (cmp(sorted(list1_rand)), sorted(list2_rand))
print (list1_rand.sort(), list2_rand.sort())
