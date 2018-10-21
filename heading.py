import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio

class HeaderBarWindow(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title="HeaderBar Demo")
		self.set_border_width(10)
		self.set_halign(Gtk.Align.FILL)
		self.set_valign(Gtk.Align.FILL)
		self.set_hexpand(True)

		#start heading
		hb = Gtk.HeaderBar()
		hb.set_show_close_button(True)
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
		#end heading

		#will add elements to the stack
		vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=1)
		stack = Gtk.Stack()
		stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
		stack.set_transition_duration(1000)

		#grid1 == first screen/element to add to stack
		grid1 = Gtk.Grid()
		element1 = Gtk.Button(label="1 Session View")
		element2 = Gtk.Button(label="2 Tag Area")
		element3 = Gtk.Button(label="3 PDML View")
		element4 = Gtk.Button(label="4 Field Area")
		#element5 = Gtk.Button(label="5 Message Type Area")
		element5 = self.messageTypeArea()

		grid1.attach(element1, 1, 1, 40, 10)
		grid1.attach_next_to(element2, element1, Gtk.PositionType.BOTTOM, 40, 10)
		grid1.attach_next_to(element3, element1, Gtk.PositionType.RIGHT, 80, 10)
		grid1.attach_next_to(element4, element3, Gtk.PositionType.BOTTOM, 40, 10)
		grid1.attach_next_to(element5, element4, 1, 40, 10)

		#add first screen/element to the stack
		stack.add_titled(grid1, "config", "Stage 1: Configuration and Setup")

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

		self.add(vbox)

	def messageTypeArea(self):
		element5 = Gtk.Notebook()
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
		element5.append_page(page1, Gtk.Label('Existing Message Type'))

		page2 = Gtk.Box()
		page2.set_border_width(10)
		page2.add(Gtk.Label('Under Construction.'))
		element5.append_page(page2, Gtk.Label('Dependency'))

		page3 = Gtk.Box()
		page3.set_border_width(10)
		page3.add(Gtk.Label('Under Construction'))
		element5.append_page(page3, Gtk.Label('Template'))

		page4 = Gtk.Box()
		page4.set_border_width(10)
		page4.add(Gtk.Label('Under Construction'))
		element5.append_page(page4, Gtk.Label('Equivalency'))

		page5 = Gtk.Box()
		page5.set_border_width(10)
		page5.add(Gtk.Label('Under Construction'))
		element5.append_page(page5, Gtk.Label('Generation'))

		return element5

win = HeaderBarWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()


