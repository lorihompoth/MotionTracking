import threading
from cameraFeed.Camera import Camera



class CameraFeed:
    def __init__(self, width, height, rotation):
        self.__cv = threading.Condition()
        self.__camera = Camera(width, height, rotation, self.__cv)

    def getFrame(self):
        with self.__cv:
            while not self.__cam.isAvailable():
                self.__cv.wait()
        return self.__cam.getSavedFrame()

