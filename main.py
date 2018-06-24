from motionTracking.MotionTracking import MotionTracking
from cameraFeed.Camera import Camera
from cameraFeed.CameraFeed import CameraFeed
import cv2
import time

print("started")

def printFps():
	fps = 1 / (time.time() - t)
	print("fps: " + str(int(fps)))
	t = time.time()

WIDTH = 432
HEIGHT = 368
FRAMERATE = 20
ROTATION = 180
print("cameraFeed()")
camFeed = CameraFeed(WIDTH, HEIGHT, ROTATION, FRAMERATE)
print("cameraFeed constructed")
mt = MotionTracking(camFeed)
print("motionTracking constructed")
t = time.time()
while True:
	image = mt.getFinal()
	printFps()

