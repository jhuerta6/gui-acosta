import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio

class HeaderBarWindow(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title="HeaderBar Demo")
		self.set_border_width(10)
		#self.set_default_size(1000, 600)
		self.set_halign(Gtk.Align.FILL)
		self.set_valign(Gtk.Align.FILL)
		self.set_hexpand(True)

		hb = Gtk.HeaderBar()
		hb.set_show_close_button(True)
		#hb.props.title = "Network Traffic Based Software Generation"
		#hb.props.title = "NTBSG"
		self.set_titlebar(hb)

		label = Gtk.Label()
		label.set_markup("<big>NTBSG</big>")
		hb.pack_start(label)

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

		vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=1)
		stack = Gtk.Stack()
		stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
		stack.set_transition_duration(1000)

		checkbutton = Gtk.CheckButton("Click me!")
		stack.add_titled(checkbutton, "config", "Stage 1: Configuration and Setup")

		label = Gtk.Label()
		label.set_markup("<big>A fancy label</big>")
		stack.add_titled(label, "message analysis", "Stage 2: Message Analysis")

		buttonwhat = Gtk.Grid()
		button1 = Gtk.Button(label="Crn 1")
		button2 = Gtk.Button(label="Crn2")
		button3 = Gtk.Button(label="Crn3")
		button4 = Gtk.Button(label="Crn4")
		button5 = Gtk.Button(label="Crn5")
		button6 = Gtk.Button(label="Crn6")

		buttonwhat.attach(button1, 1 ,1 ,1, 1)
		buttonwhat.attach(button2, 1, Gtk.PositionType.BOTTOM, 10, 2)
		buttonwhat.attach_next_to(button3, button2, Gtk.PositionType.BOTTOM, 10, 2)
		buttonwhat.attach_next_to(button4, button3, Gtk.PositionType.BOTTOM, 10, 2)
		buttonwhat.attach_next_to(button5, button4, Gtk.PositionType.BOTTOM, 10, 2)
		buttonwhat.attach_next_to(button6, button5, Gtk.PositionType.BOTTOM, 10, 2)
		stack.add_titled(buttonwhat, "sequencing", "Stage 3: Sequencing")

		phase4 = Gtk.TextView()
		stack.add_titled(phase4,"code generation","Stage 4: Code Generation")

		stack_switcher = Gtk.StackSwitcher()
		stack_switcher.set_stack(stack)
		vbox.pack_start(stack_switcher, True, True, 0)
		vbox.pack_start(stack, True, True, 0)

		grid2 = Gtk.Grid()
		button1 = Gtk.Button(label="1 Create Session")
		button2 = Gtk.Button(label="2 Open Session")
		button3 = Gtk.Button(label="3 Close Session")
		button4 = Gtk.Button(label="4 Switch Workspace")
		button5 = Gtk.Button(label="5 Open PCAP")
		button6 = Gtk.Button(label="6 Terminal")

		grid2.attach(vbox, 1, 1, 120, 10)
		#grid2.attach(button1, 1, 1, 1000, 10)
		grid2.attach_next_to(button2, vbox, Gtk.PositionType.BOTTOM, 40, 10)
		#grid2.attach_next_to(button2, button1, Gtk.PositionType.BOTTOM, 40, 10)
		grid2.attach_next_to(button3, button2, Gtk.PositionType.BOTTOM, 40, 10)
		grid2.attach_next_to(button4, button2, 1, 80, 10)
		grid2.attach_next_to(button5, button4, Gtk.PositionType.BOTTOM, 40, 10)
		grid2.attach_next_to(button6, button5, 1, 40, 10)

		self.add(grid2)

win = HeaderBarWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()


