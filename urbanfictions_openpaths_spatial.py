# import rhinoscriptsyntax as rs
import random
import datetime

class DataPoint:
	def __init__(self, _list):
		self.lat = float(_list[0])
		self.lon = float(_list[1])
		self.alt = float(_list[2])
		self.date = _list[3] ##datetime.datetime.strptime(_list[3], "%Y-%m-%d %H:%M:%S")
		self.device = _list[4]
		self.os = _list[5]
		self.version = _list[6]

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
for each in dataPoints:
    if each.lat < areaBounds[0] and each.lat > areaBounds[2] and each.lon > areaBounds[1] and each.lon < areaBounds[3]:
        myPoints.append([each.lat, each.lon, each.alt])
        myAlts.append(each.alt)
minAlt = min(myAlts)
maxAlt = max(myAlts)
# rs.AddPolyline(myPoints)
print minAlt
print maxAlt