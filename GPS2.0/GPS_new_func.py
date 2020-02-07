import os
from random import randint, choice
import GPS_point_Class
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
from collections import OrderedDict
from lxml import etree
from pykml.factory import KML_ElementMaker as KML

Nearest_points_quantity = 4
COLORS = ['7fff00ff', '7f00ff00', '7f00ffff',
		  '87000000', 'ff0000ff', 'ffff0000',
		  '7d0000ff', '7dff0000', '7d00ff00','7d00ffff']


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
			 
def search_min_dist(pholo_list):
    for i in pholo_list:
        dist_dict = {}
        for j in pholo_list:
            if i != j:
                dist = i - j
                dist_atr = {(str(j.deccoordinates[1])+','+str(j.deccoordinates[0])):dist}
                dist_dict.update(dist_atr)
        dist_atribute_dict = dict(OrderedDict(sorted(dist_dict.items(), key = lambda t : t[1])))
        while len(dist_atribute_dict) > Nearest_points_quantity:
            dist_atribute_dict.popitem()
        i.distances = dist_atribute_dict

def make_KML_placemarks(points):
	kml_list = KML.Folder()
	for i in points:
		line_color = choice(COLORS)
		line_width = randint(1,5)
		line_extrude = randint(1,5)
		point_coord = str(i.deccoordinates[1])+','+str(i.deccoordinates[0])
		near_points = list(i.distances.keys())
		doc = KML.Document(
				 
		     	KML.Placemark(KML.name(i.file_name),
			    KML.Point(KML.coordinates(point_coord))),

			    KML.Placemark(KML.Style(KML.LineStyle(KML.color(line_color), KML.width(line_width))),
					KML.LineString(KML.extrude(line_extrude),
			    KML.coordinates(point_coord+ ' ' + near_points[0]))),
			  
			    KML.Placemark(KML.Style(KML.LineStyle(KML.color(line_color), KML.width(line_width))),
					KML.LineString(KML.extrude(line_extrude),
			    KML.coordinates(point_coord + ' ' + near_points[1]))),
			  
			    KML.Placemark(KML.Style(KML.LineStyle(KML.color(line_color), KML.width(line_width))),
					KML.LineString(KML.extrude(line_extrude),
			    KML.coordinates(point_coord + ' ' + near_points[2]))),
			 
			    KML.Placemark(KML.Style(KML.LineStyle(KML.color(line_color), KML.width(line_width))),
					KML.LineString(KML.extrude(line_extrude),
			    KML.coordinates(point_coord + ' ' + near_points[3]))))

		kml_list.append(doc)
		
		#print (near_points[0]+ ' ' +near_points[1]+ ' ' +near_points[2],near_points[3])
	#print (str(etree.tostring(kml_list, pretty_print=True).decode ('utf-8')))

	f = open ('doc.kml', 'w')
	f.write (str(etree.tostring(kml_list, pretty_print=True).decode ('utf-8')))
	f.close()