import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib


packets = [["Frame718: frame, eth, ip, tcp ", ["Frame 718: 74 bytes on wire [592 bits], 74 bytes captured (592 bits) on interface 0", 25], ["Ethernet III","Internet Message Protocol", 30], ["Transmission Control Protocol", 56]]]

class PacketArea(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Packet Area")
        self.set_border_width(10)
        self.set_default_size(2000, 50)
        layout = Gtk.Box()
        self.add(layout)

        store = Gtk.TreeStore(str, int)

        for i in range(len(packets)):
            piter = store.append(None, packets[i])

            j = 1

            while j < len(packets[i]):
                store.append(piter, packets[i][j])
                j+=1






win = PacketArea()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()