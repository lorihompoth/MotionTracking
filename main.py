from motionTracking.MotionTracking import MotionTracking
from cameraFeed.Camera import Camera
from cameraFeed.CameraFeed import CameraFeed
import cv2

print("started")

WIDTH = 432
HEIGHT = 368
FRAMERATE = 20
print("camera()")
cam = Camera(WIDTH, HEIGHT, FRAMERATE)
print("camera constructed")
print("cameraFeed()")
cf = CameraFeed(cam, True, True)
print("cameraFeed constructed")
print("motionTracking()")
mt = MotionTracking(cf)
print("motionTracking constructed")
while True:
	print("motionTracking.getFinal() called")
	image = mt.getFinal()
	print("motionTracking.getFinal() finished")
	cv2.imshow("asd", image)
	print("imshow finished")
	print("execution paused")
	#input()
