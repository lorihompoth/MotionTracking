from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import threading

from cameraFeed.Preview import Preview



class Camera(threading.Thread):
    def __init__(self,cv):
        threading.Thread.__init__(self)
        self.__width = 432
        self.__height = 368
        self.__framerate = 20
        self.__rotation = 0
        self.__cv = cv
        self.__savedFrame = None
        self.__isAvailable = False
        # camera warmup:
        time.sleep(0.1)

    def getFrame(self):
        image = self.__savedFrame
        self.__savedFrame = None
        self.__isAvailable = False
        return image

    def isAvailable(self):
        return self.__isAvailable


    def getFrame(self):
        return self.__savedFrame

    def run(self):
        self.__cam = PiCamera()
        self.__cam.rotation = self.__rotation
        self.__cam.resolution = (self.__width, self.__height)
        self.__cam.framerate = self.__framerate
        self.__rawCapture = PiRGBArray(self.__cam, size=(self.__width, self.__height))

        print("camera run started")
        i = 0
        for frame in self.__cam.capture_continuous(self.__rawCapture, format="bgr", use_video_port=True):
            image = frame.array
            with self.__cv:
                self.__savedFrame = image
                self.__isAvailable = True
                self.__cv.notify()

            self.__rawCapture.truncate(0)
            i += 1

    def setResolution(self, width, height):
        self.__width = width
        self.__height = height
    def setFramerate(self, framerate):
        self.__framerate = framerate
    def setRotation(self, rotation):
        self.__rotation = rotation
