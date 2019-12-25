# Car names
list1 = []
while True:
    car_name = input ('Please insert a car name (type q to quit): ',)
    car_name1 = car_name.strip()
    car_name2 = car_name1.capitalize()
    if car_name == 'q' or 'Q' :
        break
    else :
        list1.append (car_name2)
    
print (list1)
