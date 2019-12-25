import os
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

os.chdir (r'C:\Users\AleksandrB\Desktop\Python\GPS')

def get_exif (filename) :
    exif = Image.open(filename)._getexif()
    if exif is not None :
        for key in exif.keys():
            name = TAGS.get(key,key)
        exif[name] = exif.pop(key)
        print (exif[name])
    if 'GPSInfo' in exif :
        for key in exif ['GPSInfo'].keys():
            name = GPSTAGS.get(key,key)
        exif ['GPSInfo'] [name] = exif ['GPSInfo'].pop(key)
        print (exif ['GPSInfo'] [name])
        return exif
    pass


get_exif ('2018-10-04 11.37.04.jpg')
