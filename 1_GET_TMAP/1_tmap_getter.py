import urllib.request as ur

TMAP_APP_KEY = "d43741e7-2c1b-3b9b-9513-b07e2d078883"
MIN_LAT = 37.56
MIN_LON = 126.88
MAX_LAT = 37.57
MAX_LON = 126.89
ZOOM_LEVEL = 19

OUT_DIR = "./RESULT/"

AREA_INDEX = 0
NUM = 4
for i in range(NUM):
	for j in range(NUM):
		AREA_INDEX = NUM * i + j
		in_file = ur.urlopen("https://apis.skplanetx.com/tmap/traffic?format=xml&version=1&minLat=" + str(MIN_LAT) + "&minLon=" + str(MIN_LON) + "&maxLat=" + str(MAX_LAT) + "&maxLon=" + str(MAX_LON) + "&centerLat=" + str((MIN_LAT+MAX_LAT)/2) + "&centerLon=" + str((MIN_LON+MAX_LON)/2) + "&reqCoordType=WGS84GEO&resCoordType=WGS84GEO&trafficType=AROUND&radius=5&zoomLevel=" + str(ZOOM_LEVEL) + "&sort=index&appKey=" + str(TMAP_APP_KEY))
		MIN_LAT += 0.01
		MAX_LAT += 0.01
		out_file = open(OUT_DIR+'traffic_%02d.xml' % (AREA_INDEX), 'wb')
		out_file.write(in_file.read())
		out_file.close()
	MIN_LON += 0.01
	MAX_LON += 0.01
