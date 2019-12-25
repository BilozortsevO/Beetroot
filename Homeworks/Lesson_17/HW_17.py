

class Car ():
    def __init__ (self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.speed = 0
        self.direction = ''

    def acceleration (self):
        if self.speed >=0 and self.speed <=200:
            self.speed += 1
        else:
            self.speed = 200

    def breaking (self):
        if self.speed >= 0:
            self.speed -= 1
        else:
            self.speed = 0

    def reverse (self):
        if self.speed < 0 and self.speed >-30:
            self.speed -= 1
        else:
            self.speed = -30

    def dir_North (self):
        self.direction = 'North'

    def dir_South (self):
        self.direction = 'South'

    def dir_East (self):
        self.direction = 'East'

    def dir_West (self):
        self.direction = 'West'

    def __repr__(self):
        return (self.brand, self.model, self.year, self.color,
                self.speed, self.direction)

p1_car = Car ('Nissan', 'Skyline R32', 1990, 'black')

#print(player1_car)
