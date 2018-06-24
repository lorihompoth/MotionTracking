from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import threading


class Camera(threading.Thread):
    def __init__(self, width, height, framerate, cv):
        threading.Thread.__init__(self)
        self.__width = width
        self.__height = height
        self.__framerate = framerate

        self.__cam = PiCamera()
        self.__cam.resolution = (width, height)
        self.__cam.framerate = framerate
        self.__rawCapture = PiRGBArray(self.__cam, size=(self.__width, self.__height))
        self.__sentAFrame = False

        self.__cv = cv
        self.__savedFrame = None
        self.__isAvailable = False

        time.sleep(0.1)

    def getSavedFrame(self):
        image = self.__savedFrame
        self.__savedFrame = None
        self.__isAvailable = False
        return image

    def isAvailable(self):
        return self.__isAvailable

    def run(self):
        i = 0
        for frame in self.__cam.capture_continuous(self.__rawCapture, format="bgr", use_video_port=True):
            if i > 0:
                # cv2.imshow("prev", self.__savedFrame)
                pass
            image = frame.array
            print(i)
            # cv2.imshow("camera", frame.array)
            with cv:
                # print("camera with cv")
                self.__savedFrame = image  ##not necessarily
                self.__isAvailable = True
                cv.notify()

            key = cv2.waitKey(1) & 0xFF
            self.__rawCapture.truncate(0)
            i += 1


print("started")

l = threading.Lock()
cv = threading.Condition()

WIDTH = 432
HEIGHT = 368
FRAMERATE = 15

cam = Camera(WIDTH, HEIGHT, FRAMERATE, cv)
cam.start()

while True:
    with cv:
        # print("with cv")
        while not cam.isAvailable():
            # print("waiting")
            cv.wait()
            # print("wait returned")
    image = cam.getSavedFrame()





