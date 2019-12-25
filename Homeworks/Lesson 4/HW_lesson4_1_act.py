#Guessing Game
import random

a = random.randint(1,10)
b = input ('Try to guess a number from 1 to 10: ',)
b = int (b)
if a == b :
    print ('Congratulations! You Won!')
else :
    print ('Try again.')
