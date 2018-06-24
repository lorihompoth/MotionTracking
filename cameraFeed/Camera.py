from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import threading

from cameraFeed.Preview import Preview



class Camera(threading.Thread):
    def __init__(self, width, height, rotation, framerate, cv):
        threading.Thread.__init__(self)
        self.__width = width
        self.__height = height
        self.__framerate = framerate

        self.__cam = PiCamera()
        self.__cam.rotation = rotation
        self.__cam.resolution = (width, height)
        self.__cam.framerate = framerate
        self.__rawCapture = PiRGBArray(self.__cam, size=(self.__width, self.__height))

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
        p = Preview(self.__cam)
        #p.start()
        
        i = 0
        for frame in self.__cam.capture_continuous(self.__rawCapture, format="bgr", use_video_port=True):
            image = frame.array
            #cv2.imshow("camera", frame.array)
            with self.__cv:
                #print("camera with cv")
                self.__savedFrame = image
                self.__isAvailable = True
                self.__cv.notify()

            key = cv2.waitKey(1) & 0xFF
            self.__rawCapture.truncate(0)
            i += 1
