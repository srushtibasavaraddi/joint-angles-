import argparse
import cv2
import math
 
def getAngle(a, b, c):
    ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
    return ang + 360 if ang < 0 else ang 

# initialize the list of reference points and boolean indicating
refPt = []
angles=[]

def click(event, x, y, flags, param):
	# grab references to the global variables
	global refPt
	# if the left mouse button was clicked, record the starting
	# (x, y) coordinates
	if event == cv2.EVENT_LBUTTONDOWN:
		refPt = [(x, y)]
		angles.append((x,y))

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())
# load the image, clone it, and setup the mouse callback function
image = cv2.imread(args["image"])
 
print('Original Dimensions : ',image.shape)
 
scale_percent = 10 # percent of original size
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)
# resize image
image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
print('Resized Dimensions : ',image.shape) 
clone = image.copy()
cv2.namedWindow("image")
cv2.setMouseCallback("image", click)
# keep looping until the 'q' key is pressed
while True:
	# display the image and wait for a keypress
	cv2.imshow("image", image)
	key = cv2.waitKey(1) & 0xFF
	# if the 'c' key is pressed, break from the loop
	if key == ord("c"):
		break

print("Left angles")
print("Angle alpha: ",getAngle(angles[2],angles[1],angles[0]))
print("Angle Beta: ",getAngle(angles[1],angles[2],angles[3]))
print("Right angles")
print("Angle alpha: ",getAngle(angles[6],angles[5],angles[4]))
print("Angle Beta: ",getAngle(angles[5],angles[6],angles[7]))