import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib

class FilterArea(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Filter Area")
        self.set_border_width(10)
        self.set_default_size(2000, 50)

        self.timeout_id = None

        vbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        tbox = Gtk.Box(spacing = 2)
        self.add(vbox)

        label1 = Gtk.Label("Filter Area", xalign=0)
        label2 = Gtk.Label("Saved Filter")
        tbox.pack_start(label1, True, True, 0)
        entry = Gtk.Entry()
        entry.set_text("Filter Expression")
        vbox.pack_start(tbox, True, True, 0)
        vbox.pack_start(entry, True, True, 0)

        #hbox = Gtk.Box(spacing=6)
        #vbox.pack_start(hbox, True, True, 0)

        applyBut = Gtk.Button(label="Apply")
        clearBut = Gtk.Button(label="Clear")
        saveBut = Gtk.Button(label="Save")
        saveFilters = Gtk.ComboBox()
        applyFil = Gtk.Button(label="Apply")

        vbox.pack_start(applyBut, True, True, 0)
        vbox.pack_start(clearBut, True, True, 0 )
        vbox.pack_start(saveBut, True, True, 0)
        vbox.pack_start(label2, True, True, 0)
        vbox.pack_start(saveFilters, True, True, 0)
        vbox.pack_start(applyFil, True, True, 0)
        
win = FilterArea()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
