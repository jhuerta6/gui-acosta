import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib

field = [("Frame718: frame, eth, ip, tcp", 1),
         ("Frame767: frame, eth, ip, tcp", 2), ("Frame878: frame, eth, ip, tcp", 3)]

class PacketArea(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Packet Area")
        self.set_border_width(10)
        self.set_default_size(750, 300)
        layout = Gtk.Box()
        self.add(layout)

        fieldstore = Gtk.ListStore(str, int)

        for item in field:
            fieldstore.append(list(item))
        fieldview = Gtk.TreeView(fieldstore)


        for i, coltitle in enumerate(["Packet", "Size",]):

                render = Gtk.CellRendererText()

                column = Gtk.TreeViewColumn(coltitle, render, text=i)

                fieldview.append_column(column)

        layout.pack_start(fieldview, True, True, 0)

        selectrow = fieldview.get_selection()
        selectrow.connect("changed", self.field_selected)

        bx1 = Gtk.Box(spacing=6)
        remBut = Gtk.Button(label="Remove")
        remBut.set_size_request(5, 10)
        clearBut = Gtk.Button(label="Clear")
        bx1.pack_start(remBut, True, True, 0)
        bx1.pack_start(clearBut, True, True, 0)

        layout.pack_start(bx1, True, True, 0)


    def field_selected(self, selection):
        model, row = selection.get_selected()


win = PacketArea()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()