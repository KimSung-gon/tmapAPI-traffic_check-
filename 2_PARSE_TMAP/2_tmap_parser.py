import codecs

IN_DIR = "../1_GET_TMAP/RESULT/"
OUT_DIR = "./RESULT/"

for area_index in range(16):
	in_file = codecs.open(IN_DIR+'traffic_%02d.xml' % (area_index), 'r', 'utf-8')
	out_file = open(OUT_DIR+'congestion_coor_%02d.txt' % (area_index), 'w')
	cont = in_file.read()
    # TODO: fill in this block
	key1 = "<coordinates>"
	key2 = "</coordinates>"
	key3 = "<tmap:congestion>"
	key4 = "</tmap:congestion>"
	lengthOfKey1 = len(key1)
	lengthOfKey2 = len(key2)
	lengthOfKey3 = len(key3)
	lengthOfKey4 = len(key4)
	
	start = 0
	while(start != -1):
		start = cont.find(key3, start)
		if(start != -1):		
			end = cont.find(key4, start + lengthOfKey3)
			out_file.write(cont[start+lengthOfKey3:end] + ";")
			start = cont.find(key1, end+lengthOfKey4)
			end = cont.find(key2, start + lengthOfKey1)
			coordinates = cont[start+lengthOfKey1:end]
			out_file.write(coordinates + "\n")
			start = end+lengthOfKey2

	out_file.close()
