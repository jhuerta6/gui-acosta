import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib


field = [("Frame718: frame, eth, ip, tcp", 1),
         ("Frame767: frame, eth, ip, tcp", 2), ("Frame878: frame, eth, ip, tcp", 3)]

field2 = [("icmp.type", "Type 8 [Echo [ping] request", 1, 34, 8, 8, 2),
         ("icmp.code", "Code 0", 1, 35, 0, 0, 2), ("icmp.checksum", "Checksum: 0x6861 [correct]", 0, 36, 24, 6861, 0)]


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





class FieldArea(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Field Area")
        self.set_border_width(10)
        self.set_default_size(750, 300)
        layout = Gtk.Box()
        self.add(layout)

        fieldstore = Gtk.ListStore(str, str, int , int , int, int, int)

        for item in field2:
            fieldstore.append(list(item))
        fieldview = Gtk.TreeView(fieldstore)


        for i, coltitle in enumerate(["Field Name", "Showname", "Size", "Position", "Show", "Value", "Entropy"]):

                render = Gtk.CellRendererText()

                column = Gtk.TreeViewColumn(coltitle, render, text=i)

                fieldview.append_column(column)

        layout.pack_start(fieldview, True, True, 0)

        selectrow = fieldview.get_selection()
        selectrow.connect("changed", self.field_selected)


    def field_selected(self, selection):
        model, row = selection.get_selected()


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

class HeaderBarWindow(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title="HeaderBar Demo")
		self.set_border_width(10)
		self.set_default_size(1000, 600)

		hb = Gtk.HeaderBar()
		hb.set_show_close_button(True)
		hb.props.title = "Network Traffic Based Software Generation"
		self.set_titlebar(hb)

		grid = Gtk.Grid()
		button1 = Gtk.Button(label="Create Session")
		button2 = Gtk.Button(label="Open Session")
		button3 = Gtk.Button(label="Close Session")
		button4 = Gtk.Button(label="Switch Workspace")
		button5 = Gtk.Button(label="Open PCAP")
		button6 = Gtk.Button(label="Terminal")

		grid.add(button1)
		grid.attach_next_to(button2, button1, 1, 1, 1)
		grid.attach_next_to(button3, button2, 1, 1, 1)
		grid.attach_next_to(button4, button3, 1, 1, 1)
		grid.attach_next_to(button5, button4, 1, 1, 1)
		grid.attach_next_to(button6, button5, 1, 1, 1)
		hb.pack_end(grid)

class pdml(Gtk.Window):
    def field_selected():
        print("lol")
    def __init__(self):
        Gtk.Window.__init__(self, title="PDML View")
        self.set_border_width(3)
        self.set_border_width(10)
        self.set_default_size(750, 300)

        grid= Gtk.Grid()
        self.add(grid)

        win = FilterArea()
        win.connect("destroy", Gtk.main_quit)
        #win.show_all()
        #Gtk.main()

        win4 = HeaderBarWindow()
        win4.connect("destroy", Gtk.main_quit)
        #win4.show_all()
        #Gtk.main()

        win1 = PacketArea()
        win1.connect("destroy", Gtk.main_quit)
        #win1.show_all()
        #Gtk.main()


        win2 = FieldArea()
        win2.connect("destroy", Gtk.main_quit)
        #win2.show_all()
        #Gtk.main()

        win3 = MessageTypeArea()
        win3.connect("destroy", Gtk.main_quit)
        #win3.show_all()

        grid.add(win3)
        grid.attach(win4, 1,1,1,1)
        grid.attach_next_to(win, win4, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(win1, win, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(win2, win1, Gtk.PositionType.BOTTOM, 1, 1)
        #grid.attach_next_to(win3, win2, GtK.PositionType.BOTTOM)
        #grid.attach_next_to(win2)
        #grid.add(win3)




win = pdml()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()