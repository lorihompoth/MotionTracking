import datetime
import time
import cv2

class RecordVideo:
    def __init__(self, path, width, heigth):
        self.__path = path
        ts = time.time()
        filename = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M-%S')
        self.__out = cv2.VideoWriter(path + filename + '.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (width, heigth))


        self.__i = 0

    def addFrame(self, image):
        if image is not None and self.__i < 300:
            self.__out.write(image)
            self.__i += 1
        if self.__i == 300:
            self.finish()



    def finish(self):
        self.__out.release()
