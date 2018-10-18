import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio

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

win = HeaderBarWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()