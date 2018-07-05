import threading
from cameraFeed.Camera import Camera

class CameraFeed:
    def __init__(self):
        self.__cv = threading.Condition()
        self.__camera = Camera(self.__cv)
        self.__camera.setRotation(180)
        self.__started = False


    def getFrame(self):
        if not self.__started:
            self.__camera.start()
            self.__started = True
            
        while True:
            with self.__cv:
                while not self.__camera.isAvailable():
                    self.__cv.wait()
            image = self.__camera.getFrame()
            if image is not None:
                return image
            else:
                print("CameraFeed prevented None")


    def setResolution(self, width, height):
        if not self.__started:
            self.__camera.setResolution(width, height)
            
    def setRotation(self, rotation):
        self.__camera.setRotation(rotation)
