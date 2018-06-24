from motionTracking.MotionTracking import MotionTracking
from cameraFeed.Camera import Camera
from cameraFeed.CameraFeed import CameraFeed

#heyasdasdsdfsf
WIDTH = 432
HEIGHT = 368
FRAMERATE = 20
cam = Camera(WIDTH, HEIGHT, FRAMERATE)
cf = CameraFeed(cam, True, True)
mt = MotionTracking(cf)
while True:
	image = mt.getFinal()
	cv2.imshow("asd", image)
