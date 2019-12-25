# Exclusive common numbers
import random, difflib
list1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
list1_rand = [random.randint(1,10) * 1 for list1_rand in list1]

list2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
list2_rand = [random.randint(1,10) * 1 for list2_rand in list2]

list3 = [ a, b, c, d, e, f, g, h, i, j]
print (sorted(list1_rand))
print (sorted(list2_rand))

if 1 in list1_rand and 1 in list2_rand:
    list3[0] = 1
elif 2 in list1_rand and 2 in list2_rand:
    list3[1] = 2
elif 3 in list1_rand and 3 in list2_rand:
    list3[2] = 3
elif 4 in list1_rand and 4 in list2_rand:
    list3[3] = 4
elif 5 in list1_rand and 5 in list2_rand:
    list3[4] = 5
elif 6 in list1_rand and 6 in list2_rand:
    list3[5] = 6
elif 7 in list1_rand and 7 in list2_rand:
    list3[6] = 7
elif 8 in list1_rand and 8 in list2_rand:
    list3[7] = 8
elif 9 in list1_rand and 9 in list2_rand:
    list3[8] = 9
elif 10 in list1_rand and 10 in list2_rand:
    list3[9] = 10
print (list3)

d = difflib.Differ()

list3 = d.compare(list1_rand, list2_rand)


print (list3)
    
print (list1_rand.sort(), list2_rand.sort())
