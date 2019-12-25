from random import randint as ran 

def bandit (bank):
    bet = input ('Make your bet ')
    print ('Your bet is ' + bet)
    bet = int (bet)
    input ('Press Enter to play!')
    a, b, c = ran(1,3), ran(1,3), ran(1,3)
    # Cherry
    if a == 1 and b == 1 and c == 1:
        bet *= 5
        bank += bet
        print ('You got 3x Cherries! Coefficient is 5x! The Bank is '
               + str (bank) + '\n')
    elif (a == 1 and b == 1) or (a == 1 and c == 1) or (b == 1 and c == 1):
        bet *= 1.5
        bank += bet
        print ('You got 2 Cherries! Coefficient is 1.5x! The Bank is '
               + str (bank) + '\n')

    # Bell
    elif a == 2 and b == 2 and c == 2:
        bet *= 10
        bank += bet
        print ('You got 3x Bells! Coefficient is 10x! The Bank is '
               + str (bank) + '\n')

    # 777
    elif a == 3 and b == 3 and c == 3:
        bet *= 100
        bank += bet
        print ('JACKPOT!!!! The Bank is ' + str (bank) + '\n')
    
    else:
        bank = bank - bet 
        print ('Get lucky next time! Try again! The Bank is '
               + str (bank) + '\n')
    return bank

    def res ():
        bandit (bank)

deposit = input ('Whtat\'s yours deposit? ')

for i in range (100):
    print ('The Bank is ' + str(bandit (int (deposit)))+ '\n')

