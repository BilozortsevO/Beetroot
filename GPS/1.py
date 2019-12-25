import os

points = []
for r, d, f in os.walk(path):
	for file in f:
		if file.lower().endswith(('.png','.jpg','.jpeg')):
			filepath = os.path.join(r, file)
			exif = get_exif (filepath)
			if exif is not None and 'GPSInfo' in exif:
				latlong = get_decimal_coordinates (exif['GPSInfo'])
				if latlong is not None:
					points.append (latlong) 