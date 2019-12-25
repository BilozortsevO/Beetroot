# Car names
list1 = []
while True:
    car_name = input ('Please insert a car name (type q to quit): ',)
    list1.append (car_name)
    if car_name == 'q' :
        list1.remove ('q')
        break
    continue
print (list1)
