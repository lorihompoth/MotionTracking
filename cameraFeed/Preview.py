
import time
import threading
from picamera import PiCamera
class Preview(threading.Thread):
    def __init__(self, camera):
        threading.Thread.__init__(self)
        self.__camera = camera

    def run(self):
        self.__camera.start_preview(fullscreen=False,window=(100,200,600,800))
        print("starting preview")
        time.sleep(100)
        self.__camera.stop_preview()
