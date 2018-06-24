from motionTracking.MotionTracking import MotionTracking
from cameraFeed.Camera import Camera
from cameraFeed.CameraFeed import CameraFeed
import cv2

print("started")

WIDTH = 432
HEIGHT = 368
FRAMERATE = 20
ROTATION = 180
print("cameraFeed()")
camFeed = CameraFeed(WIDTH, HEIGHT, ROTATION, FRAMERATE)
print("cameraFeed constructed")
mt = MotionTracking(camFeed)
print("motionTracking constructed")
while True:
	#print("motionTracking.getFinal() called")
	image = mt.getFinal()
	print (i)
	#print("motionTracking.getFinal() finished")
	#cv2.imshow("asd", image)
	#print("imshow finished")
	#print("execution paused")
	#input()
