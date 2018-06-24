from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2


class Camera:
    def __init__(self, width, height, framerate):
        self.__width = width
        self.__height = height
        self.__framerate = framerate

        self.__cam = PiCamera()
        self.__cam.resolution = (width, height)
        self.__cam.framerate = framerate
        self.__rawCapture = PiRGBArray(self.__cam, size=(self.__width, self.__height))

        # camera warmup:
        time.sleep(0.1)

    def getFrame(self):
        print("camera.truncate")
        #self.__rawCapture.truncate(0)
        print("camera.for")
        for frame in self.__cam.capture_continuous(self.__rawCapture, format="bgr", use_video_port=True):
            #print("camera.show preview...")
            frameCopy = frame.array.copy()
            #cv2.imshow("camera", frameCopy)
            print("camera.returning")
            return frameCopy
