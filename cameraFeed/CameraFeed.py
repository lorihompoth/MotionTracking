import threading
from cameraFeed.Camera import Camera



class CameraFeed:
    def __init__(self, width, height, rotation, framerate):
        self.__cv = threading.Condition()
        self.__camera = Camera(width, height, rotation, framerate, self.__cv)
        self.__camera.start()

    def getFrame(self):

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

