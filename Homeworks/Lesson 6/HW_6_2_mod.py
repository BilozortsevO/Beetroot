# Car names
list1 = []
while True:
    car_name = input ('Please insert a car name (type q to quit): ',)
    car_name = car_name.strip()
    
    if car_name.lower() == 'q' :
        break
    else :
        list1.append (car_name.capitalize())
    continue
print (list1)
