'''
Title: To map given coordinates to 9 identied joints in the body and calculates angle between 3 given joints
Date: 1/3/2020
Author: Srushti Basavaraddi
'''
import math
 
def getAngle(a, b, c):
    ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
    return ang + 360 if ang < 0 else ang 

x_axis=[2.4,4.3,2.4,4.4,3.6,2.5,4.8,2.6,4.5,3.7]
y_axis=[1.0,1.0,2.9,3.1,4.2,5.8,5.9,7.0,7.0,7.8]
MAX=99999

no_of_joints=9
visited=[0 for i in range(no_of_joints)]

#directory to get the co-ordinates
mapper={}

def two_points():	
	y1=min(y_axis)
	yi1=y_axis.index(y1)
	y_axis[yi1]=MAX
	y2=min(y_axis)
	yi2=y_axis.index(y2)
	x1=min(x_axis[yi1],x_axis[yi2])
	xi1=x_axis.index(x1)
	tempy=y_axis[xi1]
	if(tempy==MAX):
		tempy=y1
	tempx=x_axis[xi1]
	r1=(tempx,tempy)
	x1=max(x_axis[yi1],x_axis[yi2])
	xi1=x_axis.index(x1)
	tempy=y_axis[xi1]
	if(tempy==MAX):
		tempy=y1
	tempx=x_axis[xi1]
	r2=(tempx,tempy)
	y_axis[yi2]=MAX
	return r1,r2

def one_point():
	y1=min(y_axis)
	yi1=y_axis.index(y1)
	y_axis[yi1]=MAX
	return (x_axis[yi1],y1)
	
r1,r2=two_points()
mapper["leftFoot"]=r2
mapper["rightFoot"]=r1

r1,r2=two_points()
mapper["leftKnee"]=r2
mapper["rightKnee"]=r1

mapper["center"]=one_point()

r1,r2=two_points()
mapper["leftFist"]=r2
mapper["rightFist"]=r1

r1,r2=two_points()
mapper["leftelbow"]=r2
mapper["rightelbow"]=r1
mapper["neck"]=one_point()

print(mapper)

print(getAngle(mapper["rightFoot"],mapper["rightKnee"],mapper["center"]))




#
