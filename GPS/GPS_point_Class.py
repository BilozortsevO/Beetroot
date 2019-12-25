class Photo_data():
    def __init__ (self, file_name,date, time,
                  coordinates, deccoordinates,
                  distance1=None,distance2=None,
                  distance3=None,distance4=None):
        self.file_name = file_name
        self.date = date
        self.time = time
        self.coordinates = coordinates
        self.deccoordinates = deccoordinates
    def __str__ (self):
        return ('file_name: '+ self.file_name + '\n' + 
                'date: ' + self.date + '\n' +
                'time: ' + self.time + '\n' + 
                'coordinates: ' + self.coordinates + '\n' +
                'decimal coordinates: ' + self.deccoordinates)
