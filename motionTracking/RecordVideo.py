import datetime
import time
import cv2

class RecordVideo:
    def __init__(self, path, width, heigth):
        self.__path = path
        ts = time.time()
        filename = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M-%S')
        self.__out = cv2.VideoWriter(path + filename + '.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (width, heigth))


    def addFrame(self, image):
        self.__out.write(image)


    def finish(self):
        self.__out.release()
