import math as m

class Photo_data():
    def __init__ (self, file_name,date, time,
                  coordinates, deccoordinates,
                  distances=None):
        self.file_name = file_name
        self.date = date
        self.time = time
        self.coordinates = coordinates
        self.deccoordinates = deccoordinates
        self.distances = distances
        self.R = 6371 #Радиус Земли

    def __sub__ (self, other):

        self.distance = abs(self.R * m.acos(
                        m.sin(m.radians(self.deccoordinates[1]))*m.sin(m.radians(other.deccoordinates[1])) +
                        m.cos(m.radians(self.deccoordinates[1]))*m.cos(m.radians(other.deccoordinates[1]))*
                        m.cos(m.radians(self.deccoordinates[0]-other.deccoordinates[0]))))
        return self.distance

    def __str__ (self):
        return ('file_name: '+ self.file_name + '\n' + 
                'date: ' + self.date + '\n' +
                'time: ' + self.time + '\n' + 
                'coordinates: ' + str(self.coordinates) + '\n' +
                'decimal coordinates: ' + str(self.deccoordinates) + '\n' +
                '4 nearest points: ' + str(self.distances))
