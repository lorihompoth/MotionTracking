import threading
from cameraFeed.Camera import Camera



class CameraFeed:
    def __init__(self, width, height, rotation, framerate):
        self.__cv = threading.Condition()
        self.__camera = Camera(width, height, rotation, framerate, self.__cv)

    def getFrame(self):

        print("camFeed.getFrame/started")
        with self.__cv:
            while not self.__camera.isAvailable():
                self.__cv.wait()

        print("camFeed.getFrame/returning")
        return self.__camera.getSavedFrame()

