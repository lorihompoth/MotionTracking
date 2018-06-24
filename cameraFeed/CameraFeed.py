import threading
from cameraFeed.PrepareFrameThread import PrepareFrameThread


class CameraFeed:
    def __init__(self, camera, xFlip, yFlip):
        self.__camera = camera
        self.__xFlip = xFlip
        self.__yFlip = yFlip
        #self.__prepareThread = PrepareFrameThread(self.__camera, self.__xFlip, self.__yFlip)
        #self.__prepareThread.start()
    '''
    def getFrame(self):
        self.__prepareThread.join()
        frame = self.__prepareThread.getPreparedFrame()
        self.__prepareThread = PrepareFrameThread(self.__camera, self.__xFlip, self.__yFlip)
        self.__prepareThread.start()
        return frame
    '''
    def getFrame(self):
        return self.__camera.getFrame()


