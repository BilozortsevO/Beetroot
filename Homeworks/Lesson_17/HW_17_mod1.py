

class Car():
    def __init__ (self, brand, model, year, color,
                  speed = 0, direction = ''):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.speed = speed
        self.direction = direction

    def acceleration (self):
        if self.speed >=0 and self.speed <200:
            self.speed += 1
        else:
            self.speed = 200

    def breaking (self):
        if self.speed >= 0:
            self.speed -= 1
        else:
            self.speed = 0

#    def reverse (self):
#        if (self.speed > -30) and self.speed < 200:
#            self.speed -= 1
#        else:
#            self.speed = -30

    def dir_North (self):
        self.direction = 'North'

    def dir_South (self):
        self.direction = 'South'

    def dir_East (self):
        self.direction = 'East'

    def dir_West (self):
        self.direction = 'West'

    def __str__(self):
        return (self.brand + ' ' + self.model + ' ' + str(self.year)
                + ' ' + self.color + ' ' + str(self.speed)
                + ' ' + self.direction)

p1_car = Car ('Nissan', 'Skyline R32', 1990, 'black')

print(p1_car)

p1_car.dir_South()

for a in range (0, 211):
    p1_car.acceleration()
print(p1_car)

p1_car.dir_North()

for b in range (250, -70, -1):
    p1_car.breaking()
print(p1_car)

p1_car.dir_East()

#for c in range (250, -10, -1):
#    p1_car.reverse()
#print(p1_car)
