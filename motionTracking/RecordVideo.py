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
        self.__started = False
        self.__ts = time.time()
        self.__frameCount = 0
        self.__width = 432
        self.__height = 368

    def startFile(self):
        self.__started = True
        print("starting file")
        self.__ts = time.time()
        timestamp = datetime.datetime.fromtimestamp(self.__ts)
        if self.__path != "" and self.__path[-1] != "/": 
            self.__path += "/"
        filename = self.__path + str(timestamp.strftime('%Y-%m-%d-%H-%M-%S') + ".avi")
        self.__out = cv2.VideoWriter(filename, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 11, (self.__width, self.__height))
        pass
        
    def __recordFrame(self, image):
        print("saving frame " + str(self.__frameCount))
        self.__frameCount += 1
        image = self.timeCode(image)
        self.__out.write(image)

    def addFrame(self, image, movement):
        if self.__recordMovementOnly:
            if not movement:
                if self.__separateFiles and self.__started:
                    self.finish()
            else:
                if not self.__started:
                    self.startFile()
                self.__recordFrame(image)
        else:
            if not self.__started:
                self.startFile()
            self.__recordFrame(image)   

    def timeCode(self, image):
        if not self.__putTimecode:
            return image
        print("putting timecode") 
        font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
        lineType = 2
        position = (10, self.__height-10)
        fontColor = (255,255,255)
        #position = (self.__width, self.__height)
        text = str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H:%M:%S')) 
        cv2.putText(image, text,
                    position,
                    font,
                    self.__fontScale,
                    fontColor,
                    lineType)
        return image

    def finish(self):
        self.__started = False
        print("finishing file")
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
    def setResolution(self, width, height):
        if not self.__started:
            self.__width = width
            self.__height = height
