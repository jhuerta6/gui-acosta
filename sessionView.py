import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib

class SessionView(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Session View")
        self.set_border_width(10)
        self.set_default_size(340, 250)

        self.timeout_id = None

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        tbox = Gtk.Box(spacing = 2)
        self.add(vbox)

        label1 = Gtk.Label("Session View ", xalign=0)
        tbox.pack_start(label1, True, True, 0)
        vbox.pack_start(tbox, True, True, 0)


win = SessionView()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
