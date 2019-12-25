import os
import GPS_point_Class
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

os.chdir (r'C:\Users\AleksandrB\Documents\GitHub\Beetroot\GPS')
mainpath = r'C:\Users\AleksandrB\Documents\GitHub\Beetroot\GPS'
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

def ftime(info):
	if 'GPSTimeStamp' in info:
		i = info ['GPSTimeStamp']
		time = ( str(i[0][0]//i[0][1]) + ':'
				+ str(i[1][0]//i[1][1]) + ':'
				+ str(i[2][0]//i[2][1]))
		return time

def fdate(info):
	if 'GPSDateStamp' in info:
		j = info['GPSDateStamp'].split(':')
		date = j[-1]+'.'+j[-2]+'.'+j[-3]
		return date

def get_coordinates(info):
	for key in ['Latitude', 'Longitude']:
		if 'GPS' + key in info and 'GPS' + key + 'Ref' in info:
			e = info ['GPS' + key]
			ref = info ['GPS' + key + 'Ref']
			info [key] = ( str(int(e[0][0]/e[0][1])) + '°'
						 + str(int(e[1][0]/e[1][1])) + '′'
						 + str(e[2][0]/e[2][1]) + '″' + ref)
		if 'Latitude' in info and 'Longitude' in info:
			return [info['Latitude'], info['Longitude']]

def get_decimal_coordinates(info):
	for key in ['Latitude','Longitude']:
		if 'GPS' + key in info and 'GPS' + key + 'Ref' in info:
			e = info['GPS' + key]
			ref = info['GPS' + key + 'Ref']
			info[key] = (e[0][0]/e[0][1] +
						 e[1][0]/e[1][1]/60 +
						 e[2][0]/e[2][1]/3600) * (- 1 if ref in ['S','W'] else 1)
	if  'Latitude' in info and 'Longitude' in info:
		return [info['Latitude'], info['Longitude']]
			 
points = []
for r, d, f in os.walk(mainpath):
	for file in f:
		if file.lower().endswith(('.png','.jpg','.jpeg')):
			filepath = os.path.join(r, file)
			picture = Image.open(filepath)
			exif = getexif (picture)
			latlong = get_decimal_coordinates (exif)
			points.append (latlong)
points.sort()
#for i in range(len(points)):
#	print (points[i])
#print(fdate(getexif(original)))
#print(ftime(getexif(original)))
#print (get_coordinates (getexif(original)))
#print (get_decimal_coordinates (getexif(original)))
#print (getexif(original))
#print(original.format, original.size, original.mode)