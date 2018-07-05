import datetime
import time
import cv2

class RecordVideo:
    def __init__(self):
        self.__path = ""
        self.__putTimecode = True
        self.__fontScale = 1
        self.__recordMovementOnly = True
        self.__separateFiles = True
        ts = time.time()
        filename = str(datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M-%S')) + ".avi"
        self.__out = cv2.VideoWriter(filename, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (width, heigth))
        self.__i = 0

    def addFrame(self, image, movement):
        if movement:
            pass
        if image is not None and self.__i < 300:
            self.__out.write(image)
            self.__i += 1
        if self.__i == 300:
            self.finish()



    def finish(self):
        self.__out.release()
        
    def setDestinationFolder(self, destinationFolder):
        self.__path = destinationFolder
    def setPutTimecode(self, putTimecode):
        self.__putTimecode = putTimecode
    def setFontScale(self, fontScale):
        self.__fontScale = fontScale
    def setRecordMovementOnly(self, recordMovementOnly):
        self.__recordMovementOnly = recordMovementOnly
    def setSeparateFiles(self, separateFiles):
        self.__separateFiles = separateFiles
