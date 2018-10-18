import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MessageTypeArea(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Message Type Area")
        self.set_border_width(3)
        self.set_border_width(10)
        self.set_default_size(750, 300)

        notebook = Gtk.Notebook()
        self.add(notebook)

        page1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        page1.set_border_width(10)
        bx1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        bx2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        page1.add(Gtk.Label('New Modify'))
        bx1.add(Gtk.Label('Message Type Name'))
        bx1.pack_start(Gtk.Entry(), True, True, 10)
        bx2.add(Gtk.Label('Message Type Field Value Pairs'))
        bx2.pack_start(Gtk.Entry(), True, True, 10)
        bx3 = Gtk.Box()
        existing_msg_types = Gtk.ComboBox()
        #existing_msg_types.config(height = 1, width= 3)
        page1.pack_start(existing_msg_types, True, True, 10)
        page1.pack_start(bx1, True, True, 10)
        page1.pack_start(bx2, True, True, 10)
        deleteBut = Gtk.Button(label="Delete")
        saveBut = Gtk.Button(label="Save")
        clearBut = Gtk.Button(label="Clear")
        bx3.pack_start(deleteBut, True, True, 0)
        bx3.pack_start(saveBut, True, True, 0 )
        bx3.pack_start(clearBut, True, True, 0)
        page1.pack_start(bx3, True, True, 0)
        notebook.append_page(page1, Gtk.Label('Existing Message Type'))


        page2 = Gtk.Box()
        page2.set_border_width(10)
        page2.add(Gtk.Label('Under Construction.'))
        notebook.append_page(page2, Gtk.Label('Dependency'))

        page3 = Gtk.Box()
        page3.set_border_width(10)
        page3.add(Gtk.Label('Under Construction'))
        notebook.append_page(page3, Gtk.Label('Template'))

        page4 = Gtk.Box()
        page4.set_border_width(10)
        page4.add(Gtk.Label('Under Construction'))
        notebook.append_page(page4, Gtk.Label('Equivalency'))

        page5 = Gtk.Box()
        page5.set_border_width(10)
        page5.add(Gtk.Label('Under Construction'))
        notebook.append_page(page5, Gtk.Label('Generation'))
