import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="New Session")
        self.set_border_width(10)
        self.set_size_request(500, 300)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        label = Gtk.Label("Create a new session.")
        label.set_justify(Gtk.Justification.CENTER)
        vbox.pack_start(label, False, True, 10) #child, expand, fill, padding

        #top section
        boxTop = Gtk.Box(spacing=6)
        vbox.pack_start(boxTop, False, True, 0)

        label = Gtk.Label("Session Name")
        boxTop.pack_start(label, False, True, 10)

        self.entry = Gtk.Entry()
        # self.entry.set_placeholder_text("Project Name")
        self.entry.set_width_chars(50)
        boxTop.pack_start(self.entry, True, True, 10)

        #middle section
        boxMid = Gtk.Box(spacing=6)
        vbox.pack_start(boxMid, True, True, 0)

        label = Gtk.Label("Description     ")
        boxMid.pack_start(label, False, True, 10)

        self.textview = Gtk.TextView()
        self.textbuffer = self.textview.get_buffer()
        # self.textbuffer.set_text("Project Description")
        self.textview.set_size_request(420, -1)
        boxMid.pack_start(self.textview, True, True, 10)

        #bottom section (Buttons)
        boxBot = Gtk.Box(spacing=6)
        vbox.pack_start(boxBot, False, True, 10)

        self.button1 = Gtk.Button(label="Cancel")
        self.button1.connect("clicked", Gtk.main_quit)
        boxBot.pack_end(self.button1, False, False, 10)

        self.button2 = Gtk.Button(label="Create")
        self.button2.connect("clicked", Gtk.main_quit)
        boxBot.pack_end(self.button2, False, False, 0)

    def on_button_clicked(self, widget):
        pass

win = MyWindow()
win.set_position(Gtk.WindowPosition.CENTER)
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()