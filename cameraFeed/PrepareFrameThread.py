import threading
import cv2


class PrepareFrameThread(threading.Thread):
    def __init__(self, camera, xFlip, yFlip):
        threading.Thread.__init__(self)
        self.__camera = camera
        self.__xFlip = xFlip
        self.__yFlip = yFlip

    def run(self):
        self.__frame = self.__camera.getFrame()
        self.__doTheFlips()

    def __doTheFlips(self):
        if self.__xFlip and self.__yFlip:
            imageCopy = self.__frame.copy()
            image = cv2.flip(imageCopy, 0)  # xFLip
            self.__frame = cv2.flip(image, 1)  # yFlip

    def getPreparedFrame(self):
        return self.__frame
