import rhinoscriptsyntax as rs
import datetime

class DataPoint:
	def __init__(self, _list):
		self.lat = float(_list[0])
		self.lon = float(_list[1])
		self.alt = float(_list[2])
		self.date = _list[3] #datetime.datetime.strptime(_list[3], "%Y-%m-%d %H:%M:%S")
		self.device = _list[4]
		self.os = _list[5]
		self.version = _list[6]

def reMapVals(x, in_min, in_max, out_min, out_max):
	return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

areaBounds = [40.944639,-74.465332, 40.446947,-73.531494]

dataPoints = []
#myRawData = open('openpaths_falets.csv')
counter = 0
for line in open('openpaths_falets.csv'):
    if counter == 0:
		pass
    else:
        dataPoints.append(DataPoint(line.split(',')))
    counter += 1
myPoints = []
myAlts = []
for each in dataPoints: #pull the focus area, based on map coordinates defined in 'areaBounds' vairable
    if each.lat < areaBounds[0] and each.lat > areaBounds[2] and each.lon > areaBounds[1] and each.lon < areaBounds[3]:
        myPoints.append([each.lat, each.lon, each.alt])
        myAlts.append(each.alt)
minAlt = min(myAlts)
maxAlt = max(myAlts)
lineSet = []
for each in myPoints: #normalize the z-values
	each[2] = reMapVals(each[2], minAlt, maxAlt, -.1, .1)
for index in range(len(myPoints)):
	if index == len(myPoints)-1:
		break
	else:
		lineSet.append(rs.AddLine(myPoints[index], myPoints[index+1]))
nurbsPipe = []
for index, item in enumerate(lineSet):
	# if index > 0:
	# 	oldPipe = nurbsPipe
	# 	surfaces = [nurbsPipe, oldPipe]
	# 	rs.BooleanUnion(surfaces)
	nurbsPipe = rs.AddPipe(item, 0, .005, cap=2)
	rs.DeleteObject(item)