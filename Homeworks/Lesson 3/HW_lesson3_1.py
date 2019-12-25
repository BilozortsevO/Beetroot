phone_num = input ('Please insert your actual phone number: ')
phone_length = 10
phone_str = phone_num
if len(phone_str, ) == phone_length :
    try:
        phone_num = int (phone_num)
                   
    except ValueError:
        print ('Your phone number is:', phone_num)
else :
    print ('The wrong format of the phone number!')
