import time
import sys
sys.path.append('/usr/local/lib/python3.10/dist-packages/')
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf, GLib

class TuxAnimation:
    def __init__(self):
        self.i = 0
        self.direction = 15
        self.builder = Gtk.Builder()
        self.builder.add_from_file("image/tux_animation.glade")
        self.builder.connect_signals(self)
        self.image = self.builder.get_object("tux_image")
        self.window = self.builder.get_object("main_window")
        self.window.move(0,850)
        self.window.connect("destroy", Gtk.main_quit)
        self.window.set_opacity(0.5) 
        self.image.connect("activate", self.hey)
        self.window.show_all()
        self.gif = GdkPixbuf.PixbufAnimation.new_from_file("image/tuxwalk.gif")
        self.iter = self.gif.get_iter()
        self.image.set_from_pixbuf(self.iter.get_pixbuf())
        self.walk()
        time.sleep(1)

    def on_destroy(self, *args):
        Gtk.main_quit()

    def walk(self):
        if self.i >= 375:
            self.direction = -15
        elif self.i <= 15:
            self.direction = 15
        self.i += self.direction
        self.image.set_margin_start(self.i)
        if self.iter.advance():
            self.image.set_from_pixbuf(self.iter.get_pixbuf())
        GLib.timeout_add(150, self.walk)
        

    def hey(self, widget, event):
        gif = GdkPixbuf.PixbufAnimation.new_from_file("image/tux02.gif")
        self.image.set_from_animation(gif)
     

if __name__ == "__main__":
    TuxAnimation()
    Gtk.main()
