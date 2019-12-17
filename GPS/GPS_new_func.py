import os
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

os.chdir (r'C:\Users\AleksandrB\Documents\GitHub\Beetroot\GPS')

try:  
	original = Image.open('2019-08-21 17.33.37.jpg')  
except FileNotFoundError:  
	print('Файл не найден')


def getexif(filename):
	exif = filename._getexif()
	if exif is not None :
		for key1, value in exif.items():
			if TAGS.get(key1,key1) == 'GPSInfo':
				gpstags = {GPSTAGS.get(key,key):exif[key1].get(key) \
					for key in value.keys()}
	return gpstags

			
print (getexif(original))
 			
#print (gpstags)
#print (tag)
#print (gpstag)
#print("The size of the Image is: ")  
#print(original.format, original.size, original.mode)