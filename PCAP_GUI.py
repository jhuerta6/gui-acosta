import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="PCAP")
        self.set_border_width(10)
        self.set_size_request(400, 300)

        vboxOuter = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        self.add(vboxOuter)


        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        vboxOuter.pack_start(vbox, True, True, 0)

        label = Gtk.Label("Open a PCAP File")
        vbox.pack_start(label, False, True, 10) #child, expand, fill, padding

        #top section
        boxTop = Gtk.Box(spacing=6)
        vbox.pack_start(boxTop, False, True, 0)

        label = Gtk.Label("PCAP Name         ")
        boxTop.pack_start(label, False, True, 0)

        self.entry = Gtk.Entry()
        # self.entry.set_placeholder_text("PCAP File")
        self.entry.set_width_chars(50)
        boxTop.pack_start(self.entry, True, True, 10)

        #middle section
        boxMid = Gtk.Box(spacing=6)
        vbox.pack_start(boxMid, True, True, 0)

        label = Gtk.Label("Dissector Name")
        boxMid.pack_start(label, False, True, 0)


        self.textview = Gtk.TextView()
        self.textbuffer = self.textview.get_buffer()
        self.textbuffer.set_text("")
        boxMid.pack_start(self.textview, True, True, 10)

        #bottom section (Buttons)
        boxBot = Gtk.Box(spacing=6)
        vbox.pack_start(boxBot, False, True, 10)

        self.button1 = Gtk.Button(label="Cancel")
        self.button1.connect("clicked", Gtk.main_quit)
        boxBot.pack_end(self.button1, False, False, 10)

        self.button2 = Gtk.Button(label="Convert to PDML")
        self.button2.connect("clicked", Gtk.main_quit)
        boxBot.pack_end(self.button2, False, False, 0)

        vboxRight = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)
        vboxOuter.pack_end(vboxRight, False, True, 0)

        label = Gtk.Label("")
        vboxRight.pack_start(label, False, True, 10) #child, expand, fill, padding

        self.btnPCAPBrowse = Gtk.Button(label="Browse")
        self.btnPCAPBrowse.connect("clicked", self.on_button_clicked)
        vboxRight.pack_start(self.btnPCAPBrowse, False, False, 0)

        self.btnDissBrowse = Gtk.Button(label="Browse")
        self.btnDissBrowse.connect("clicked", self.on_button_clicked)
        vboxRight.pack_start(self.btnDissBrowse, False, False, 0)

        label = Gtk.Label("")
        vboxRight.pack_start(label, False, True, 10) #child, expand, fill, padding

    def on_button_clicked(self, widget):
        pass

win = MyWindow()
win.set_position(Gtk.WindowPosition.CENTER)
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()