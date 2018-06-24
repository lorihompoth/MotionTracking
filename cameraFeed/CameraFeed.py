import threading
from cameraFeed.PrepareFrameThread import PrepareFrameThread


class CameraFeed:
    def __init__(self, camera, xFlip, yFlip):
        self.__camera = camera
        self.__xFlip = xFlip
        self.__yFlip = yFlip
        self.__frameLock = threading.Lock()
        self.__prepareThread = PrepareFrameThread(self.__camera, self.__frameLock, self.__xFlip, self.__yFlip)

    def getFrame(self):
        self.__frameLock.acquire()
        frame = self.__prepareThread.getPreparedFrame()
        self.__frameLock.release()
        self.__prepareThread.start()
        return frame



