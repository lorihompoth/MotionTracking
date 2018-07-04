from view.Gui import Gui
print("Gui started")
Gui()
print("gui terminated")
'''

from motionTracking.MotionTracking import MotionTracking
from cameraFeed.Camera import Camera
from cameraFeed.CameraFeed import CameraFeed
import cv2
import time



WIDTH = 432
HEIGHT = 368
FRAMERATE = 20
ROTATION = 180
camFeed = CameraFeed(WIDTH, HEIGHT, ROTATION, FRAMERATE)
#print(self.__destinationFolder[7:])
mt = MotionTracking(camFeed, None)
t = time.time()
while True:
    image = mt.getFinal()
    if image is not None:
        #cv2.imshow("asd", image)
        fps = 1/(time.time() - t)
        print("fps: " + str(int(fps)))
        t = time.time()
'''