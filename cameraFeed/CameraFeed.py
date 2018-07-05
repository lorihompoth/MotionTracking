import threading
from cameraFeed.Camera import Camera

class CameraFeed:
    def __init__(self):
        self.__cv = threading.Condition()
        self.__camera = Camera(self.__cv)
        self.__camera.setRoration(180)
        self.__started = False


    def getFrame(self):
        if not self.__started:
            self.camera.start()
            self.__started = True
            
        print("camFeed.getFrame/started")
        while True:
            with self.__cv:
                while not self.__camera.isAvailable():
                    self.__cv.wait()
            print("camFeed.getFrame/notified for new frame")
            image = self.__camera.getFrame()
            print("camFeed.getFrame/got new frame")
            if image is not None:
                    
                print("camFeed.getFrame/returning")
                return image
            else:
                print("CameraFeed prevented None")


    def setResolution(self, width, height):
        if not self.__started:
            self.__camera.setResolution(width, height)
            
    def setRotation(self, rotation):
        self.__camera.setRoration(rotation)