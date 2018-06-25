import gi # for GUI

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Gui:
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
        self.__preview = self.__builder.get_object("checkbutton11").get_active()
        self.__finalScreen = self.__builder.get_object("checkbutton1").get_active()
        self.__phase1 = self.__builder.get_object("checkbutton2").get_active()
        self.__phase2 = self.__builder.get_object("checkbutton3").get_active()
        self.__phase3 = self.__builder.get_object("checkbutton4").get_active()
        self.__phase4 = self.__builder.get_object("checkbutton5").get_active()
        self.__phase5 = self.__builder.get_object("checkbutton6").get_active()
        self.__recordVideo = self.__builder.get_object("checkbutton7").get_active()
        self.__destinationFolder = self.__builder.get_object("filechooserbutton1").get_uri()
        self.__putTimecode = self.__builder.get_object("checkbutton8").get_active()
        self.__fontSize = self.__builder.get_object("entry5").get_text()
        self.__recordContinously = self.__builder.get_object("radiobutton1").get_active()
        self.__recordMovement = self.__builder.get_object("radiobutton2").get_active()
        self.__intoASingleFile = self.__builder.get_object("radiobutton3").get_active()
        self.__separateFiles = self.__builder.get_object("radiobutton4").get_active()
        self.__resolution = self.__builder.get_object("comboboxtext1").get_active_text()
        self.__aimTowardsMotion = self.__builder.get_object("checkbutton9").get_active()
        self.__aimWithArrowKeys = self.__builder.get_object("checkbutton10").get_active()
        self.__blur = self.__builder.get_object("entry1").get_text()
        self.__threshold = self.__builder.get_object("entry6").get_text()
        self.__standbyBetweenMovements = self.__builder.get_object("entry2").get_text()
        self.__cameraFieldOfView = self.__builder.get_object("entry4").get_text()
        self.__minTrigger = self.__builder.get_object("entry3").get_text()



