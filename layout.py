import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

from pdml_view import create_pdml_view

class layout(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title="Network Traffic Based Software Generation")
        self.set_border_width(10)
        self.set_default_size(2000,2000)

        ## Main Container ##
        main = Gtk.Grid()
        self.add(main)

        ## Fill Main Container ##
        pdml_view = create_pdml_view()
        main.add(pdml_view)



win = layout()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
