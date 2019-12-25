# checking of correct phone number input
phone_num = input ('Please insert your actual phone number: ')

phone_length = 10

if len(phone_num, ) == phone_length and phone_num.isdigit() == True:

    print ('Your phone number is:', phone_num)
    
else :
    
    print ('The wrong format of the phone number!')
