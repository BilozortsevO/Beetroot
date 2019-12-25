import os
from GPS_new_func import *
from GPS_point_Class import * 
from lxml import etree
from pykml.factory import KML_ElementMaker as KML

#if os.path.exists(os.getcwd()+'\IN_PHOTO'):
#    os.chdir(os.getcwd()+'\IN_PHOTO')
#else:
#    newdir = input('Введите адрес директории: ')
#    os.chdir (newdir)

os.chdir (r'C:\Users\AleksandrB\Documents\GitHub\Beetroot\GPS')
print ('Текущая директория: ' + str(os.getcwd()))

file_list = os.listdir(os.getcwd())
pictures_list = list(filter(lambda x: x.endswith('.jpg'), file_list))
points = []
try:
    for r, d, f in os.walk(os.getcwd()):
        for file in pictures_list:
            filepath = os.path.join(r, file)
            picture = Image.open(filepath)
            exif = getexif (picture)
            date = fdate (exif)
            time = ftime (exif)
            latlong = get_coordinates(exif)
            declatlong = get_decimal_coordinates (exif)
            pic = Photo_data(str(file), str(date),
                             str(time), str(latlong),
                             str(declatlong))
            points.append (pic)
except FileNotFoundError:
    pass

f = open ('doc.kml', 'w')

kml_list = KML.Folder()

for i in points:
    lat_long = i.coordinates.split(',')
    doc = KML.kml(
    KML.Placemark(
        KML.name(i.file_name),
        KML.LookAt(KML.latitude(lat_long[0]),
                   KML.longitude(lat_long[1])
        #,KML.LineString(KML.extrude('1'),
        #              KML.coordinates(),
                  ),
                  ),
                  )
    f = open ('doc.kml', 'a')
    kml_list.append(doc)
print (etree.tostring(kml_list))
f.write (str(etree.tostring(kml_list)))

    
    

#print(points[0])

for i in points:
    print (i)

#os.rename(src, dst, *, src_dir_fd=None, dst_dir_fd=None)
