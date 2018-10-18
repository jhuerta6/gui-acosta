import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib

field = [("icmp.type", "Type 8 [Echo [ping] request", 1, 34, 8, 8, 2),
         ("icmp.code", "Code 0", 1, 35, 0, 0, 2), ("icmp.checksum", "Checksum: 0x6861 [correct]", 0, 36, 24, 6861, 0)]

class FieldArea(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Field Area")
        self.set_border_width(10)
        self.set_default_size(750, 300)
        layout = Gtk.Box()
        self.add(layout)

        fieldstore = Gtk.ListStore(str, str, int , int , int, int, int)

        for item in field:
            fieldstore.append(list(item))
        fieldview = Gtk.TreeView(fieldstore)


        for i, coltitle in enumerate(["Field Name", "Showname", "Size", "Position", "Show", "Value", "Entropy"]):

                render = Gtk.CellRendererText()

                column = Gtk.TreeViewColumn(coltitle, render, text=i)

                fieldview.append_column(column)

        layout.pack_start(fieldview, True, True, 0)

        selectrow = fieldview.get_selection()
        selectrow.connect("changed", self. field_selected)


    def field_selected(self, selection):
        model, row = selection.get_selected()




win = FieldArea()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()