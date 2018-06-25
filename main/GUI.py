import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Handler:
    def onDestroy(self, *args):
        Gtk.main_quit()

    def onButtonPressed(self, button):
        print("Hello World!")

    def checkbutton11_toggled_cb(self, button):
        builder.get_object("checkbutton11").getText()
        print("button toggled")

    def activateed(self):
        print("font size")


builder = Gtk.Builder()
builder.add_from_file("gui.glade")
builder.connect_signals(Handler())

window = builder.get_object("dialog1")
asd = builder.get_object("checkbutton11")
window.show_all()

Gtk.main()



