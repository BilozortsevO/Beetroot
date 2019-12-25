# average
import random

x = random.randint(0,100)
y = random.randint(0,100)

z = (x + y) / 2

print ('You should calculate the average of the next two numbers: ', x, y)

result = input ('Please insert the average result of the next numbers: ', )

if float(result) == z:
    print ("It's a right answer!")
    
else :
    print ("Sorry, but it's a wrong answer")
