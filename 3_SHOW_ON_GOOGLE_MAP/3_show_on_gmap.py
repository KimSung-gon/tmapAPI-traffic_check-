import webbrowser

GOOGLE_APP_KEY = 'AIzaSyCOnkRr_swB0ls1GBTqPSTDSMYNEYFYEys'
CENTER = '37.60,126.90'

IN_DIR = '../2_PARSE_TMAP/RESULT/'
OUT_DIR = './RESULT/'

for area_index in range(16):
	in_file = open(IN_DIR + "congestion_coor_%02d.txt" % (area_index), 'r')
	out_file = open(OUT_DIR + "gmap_urlstr_%02d.txt" % (area_index), 'w')
	paths = ''
	for line in in_file:
		congestion, linestring = line.split(';')
		if congestion != '0' and congestion != '1':
			paths += '&path=color:'
			if congestion == '2':
				paths += 'green'
			if congestion == '3':
				paths += 'yellow'
			if congestion == '4':
				paths += 'orange'
			if congestion == '5':
				paths += 'red'
			paths += '|weight:5|'
			first,rest = linestring.split(' ', maxsplit=1)
			last = ''.join(linestring.rsplit(' ', 1)[1])
			lon1,lat1 = first.split(',', maxsplit=1)
			lon2,lat2 = last.split(',', maxsplit=1)
			paths += lat1 + ',' + lon1 + '|' + lat2 + ',' + lon2
	
	urlstr = ("https://maps.googleapis.com/maps/api/staticmap?key="+ GOOGLE_APP_KEY + "&center=" + CENTER + "&zoom=12&size=600x600&maptype=roadmap" + paths)
	webbrowser.open(urlstr)
	out_file.write(urlstr)
	out_file.close()

