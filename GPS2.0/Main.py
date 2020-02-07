import os
from GPS_new_func import *
from GPS_point_Class import * 


#if os.path.exists(os.getcwd()+'\IN_PHOTO'):
#    os.chdir(os.getcwd()+'\IN_PHOTO')
#else:
#    newdir = input('Введите адрес директории: ')
#    os.chdir (newdir)


os.chdir (r'C:\Users\AleksandrB\Documents\GitHub\Beetroot\GPS2.0')
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
                             str(time), latlong,
                             declatlong)
            points.append (pic)
except FileNotFoundError:
    pass


search_min_dist(points)

print (points[1])

make_KML_placemarks(points)


#os.rename(src, dst, *, src_dir_fd=None, dst_dir_fd=None)
