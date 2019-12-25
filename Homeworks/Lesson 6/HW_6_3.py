# List reverse

list1 = ['Denza ','Faradenza', 'La', 'bokka', 'de', 'la', 'cokka',
         'Grande', 'love', 'and', 'ribaua', 'villa', 'vida', 'loca']
list2 = []
print (list1)

for i in range (len(list1)):
    
    list2.append(list1[(i+1)* (-1)]) 

print (list2)


