import threading
import sys
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib, GdkPixbuf
from Read2 import*

class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Puzzle2_v4")
        
        self.general_box=Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=1)
        self.add(self.general_box)
        
        self.box=Gtk.Box(spacing=1)
        self.box.set_homogeneous(False)
        self.clear_box=Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.clear_box.set_homogeneous(False)
        
        self.general_box.pack_start(self.box, True, True, 0)
        self.general_box.pack_start(self.clear_box, True, True, 0)
        
        pixbuf= GdkPixbuf.Pixbuf.new_from_file_at_scale(filename="logo.png", width=150, height=150, preserve_aspect_ratio=True)
        self.image= Gtk.Image.new_from_pixbuf(pixbuf)
        self.image.set_name("image")
        self.box.add(self.image)
        
        self.label =Gtk.Label()
        self.label.set_name("blue_label")
        self.label.set_markup("Please, login with your <big>UID</big> \n \n <small> Raquel Abad de las Heras </small>")
        self.label.set_justify(Gtk.Justification.CENTER)
        self.label.set_size_request(400,150)
        self.box.pack_start(self.label, True,True, 0)
        

        
        self.button = Gtk.Button.new_with_label("Clear")
        self.button.set_name("blue_button")
        self.button.connect("clicked", self.on_button_clicked)
        self.clear_box.pack_start(self.button, True, True, 0)
        
        blue_style = Gtk.CssProvider()
        css= '#blue_label{ background-color: #cce6ff; color: #003566; } #blue_button{ background-color: #003566; color:#ffffff}'
        blue_style.load_from_data(css.encode('ascii'))
        
        Gtk.StyleContext.add_provider(self.label.get_style_context(),  blue_style, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
        Gtk.StyleContext.add_provider(self.button.get_style_context(),  blue_style, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
        
        
    def on_button_clicked(self, widget):
        self.label.set_markup("Please, login with your <big>UID</big> \n \n <small> Raquel Abad de las Heras </small>")
        global thread
        if not thread.isAlive():
            thread = threading.Thread(target=read)
            thread.start()
            

def read():
    rf=Rfid_Reader()
    uid=rf.read_uid()
    GLib.idle_add(win.label.set_markup('uid:<big><b>'+uid+'</b></big>'))
    
if __name__ == "__main__":
    
    win = MyWindow()
    
    thread = threading.Thread(target=read)
    thread.start()

    
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    
    Gtk.main()
