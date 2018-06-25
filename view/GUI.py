import gi # for GUI

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from motionTracking.MotionTracking import MotionTracking
from cameraFeed.Camera import Camera
from cameraFeed.CameraFeed import CameraFeed
from view.GUI import GUI
import cv2
import time

class GUI:
    def __init__(self):
        # def initializeGUI():
        self.__builder = Gtk.Builder()
        self.__builder.add_from_file("gui.glade")
        self.__builder.connect_signals(self)
        window = self.__builder.get_object("dialog1")
        window.show_all()
        Gtk.main()

    def onDestroy(self, *args):
        Gtk.main_quit()

    def exitButton(self, button):
        exit(0)

    def on_button2_clicked(self, arg1):
        self.__preview = builder.get_object("checkbutton11").get_active()
        self.__finalScreen = builder.get_object("checkbutton1").get_active()
        self.__phase1 = builder.get_object("checkbutton2").get_active()
        self.__phase2 = builder.get_object("checkbutton3").get_active()
        self.__phase3 = builder.get_object("checkbutton4").get_active()
        self.__phase4 = builder.get_object("checkbutton5").get_active()
        self.__phase5 = builder.get_object("checkbutton6").get_active()
        self.__recordVideo = builder.get_object("checkbutton7").get_active()
        self.__destinationFolder = builder.get_object("filechooserbutton1").get_uri()
        self.__putTimecode = builder.get_object("checkbutton8").get_active()
        self.__fontSize = builder.get_object("entry5").get_text()
        self.__recordContinously = builder.get_object("radiobutton1").get_active()
        self.__recordMovement = builder.get_object("radiobutton2").get_active()
        self.__intoASingleFile = builder.get_object("radiobutton3").get_active()
        self.__separateFiles = builder.get_object("radiobutton4").get_active()
        self.__resolution = builder.get_object("comboboxtext1").get_active_text()
        self.__aimTowardsMotion = builder.get_object("checkbutton9").get_active()
        self.__aimWithArrowKeys = builder.get_object("checkbutton10").get_active()
        self.__blur = builder.get_object("entry1").get_text()
        self.__threshold = builder.get_object("entry6").get_text()
        self.__standbyBetweenMovements = builder.get_object("entry2").get_text()
        self.__cameraFieldOfView = builder.get_object("entry4").get_text()
        self.__minTrigger = builder.get_object("entry3").get_text()


    def run(self):
        print("started")
        WIDTH = 432
        HEIGHT = 368
        FRAMERATE = 20
        ROTATION = 180
        print("cameraFeed()")
        camFeed = CameraFeed(WIDTH, HEIGHT, ROTATION, FRAMERATE)
        print("cameraFeed constructed")
        mt = MotionTracking(camFeed)
        print("motionTracking constructed")
        t = time.time()
        while True:
            image = mt.getFinal()
            if image is not None:

                cv2.imshow("asd", image)
            else:
                print("Main Prevented None")
            # fps = 1/(time.time() - t)
            # print("fps: " + str(int(fps)))
            t = time.time()



