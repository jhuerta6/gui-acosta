import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio

class mainWindow(Gtk.Window):
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
		element2 = self.tagArea()
		#element3 = Gtk.Button(label="3 PDML View")
		element3 = self.pdmlView()
		element4 = self.fieldAreaMessageTypeArea()

		grid1.attach(element1, 1, 1, 40, 10)
		grid1.attach_next_to(element2, element1, Gtk.PositionType.BOTTOM, 40, 10)
		grid1.attach_next_to(element3, element1, Gtk.PositionType.RIGHT, 80, 10)
		grid1.attach_next_to(element4, element3, Gtk.PositionType.BOTTOM, 80, 10)

		#add first screen/element to the stack
		stack.add_titled(grid1, "config", "Stage 1: Configuration and Setup")

		label = Gtk.Label()
		label.set_markup("<big>A fancy label</big>")
		stack.add_titled(label, "message analysis", "Stage 2: Message Analysis")

		grid3 = Gtk.Grid()
		button1 = Gtk.Button(label="Crn 1")
		button2 = Gtk.Button(label="Crn2")
		button3 = Gtk.Button(label="Crn3")
		button4 = Gtk.Button(label="Crn4")
		button5 = Gtk.Button(label="Crn5")
		button6 = Gtk.Button(label="Crn6")

		grid3.attach(button1, 1 ,1 ,1, 1)
		grid3.attach(button2, 1, Gtk.PositionType.BOTTOM, 10, 2)
		grid3.attach_next_to(button3, button2, Gtk.PositionType.BOTTOM, 10, 2)
		grid3.attach_next_to(button4, button3, Gtk.PositionType.BOTTOM, 10, 2)
		grid3.attach_next_to(button5, button4, Gtk.PositionType.BOTTOM, 10, 2)
		grid3.attach_next_to(button6, button5, Gtk.PositionType.BOTTOM, 10, 2)
		stack.add_titled(grid3, "sequencing", "Stage 3: Sequencing")

		phase4 = Gtk.TextView()
		stack.add_titled(phase4,"code generation","Stage 4: Code Generation")

		stack_switcher = Gtk.StackSwitcher()
		stack_switcher.set_stack(stack)
		vbox.pack_start(stack_switcher, True, True, 0)
		vbox.pack_start(stack, True, True, 0)

		self.add(vbox)

	def fieldAreaMessageTypeArea(self):
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
	def tagArea(self):
		main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=400)

		## Sub Containers ##
		tag_box = Gtk.Grid()
		confirm_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=4)
		main_box.pack_start(tag_box, True, True, 0)
		main_box.pack_start(confirm_box, True, True, 0)

		## Drop down tags and entries ##
		saved_tag = Gtk.ComboBoxText()
		tag_name = Gtk.Entry()
		tag_name.set_text("Tag Name")
		tagged_field = Gtk.Entry()
		tagged_field.set_text("Tagged Field")
		tag_description = Gtk.Entry()
		tag_description.set_text("Tag Description")

		saved_tag_label = Gtk.Label("Saved Tag")
		tag_name_label = Gtk.Label("Tag Name")
		tagged_field_label = Gtk.Label("Tagged Field")
		tag_description_label = Gtk.Label("Tag Description")

		## Action Buttons ##
		update_button = Gtk.Button.new_with_label("Update")
		cancel_button = Gtk.Button.new_with_label("Cancel")

		## Added to respective Containers ##
		tag_box.add(saved_tag_label)
		tag_box.attach(saved_tag, 1, 0, 1, 1)
		tag_box.attach(tag_name_label, 0, 1, 1, 1)
		tag_box.attach(tag_name, 1, 1, 1, 1)
		tag_box.attach(tagged_field_label, 0, 2, 1, 1)
		tag_box.attach(tagged_field, 1, 2, 1, 1)
		tag_box.attach(tag_description_label,0, 3, 1, 1)
		tag_box.attach(tag_description,1, 3, 1, 1)

		confirm_box.pack_start(update_button, True, True, 0)
		confirm_box.pack_start(cancel_button, True, True, 0)
		return main_box
	def pdmlView(self):
		main_box = Gtk.Grid()
		menu = Gtk.Grid()
		entry1 = Gtk.Entry()
		entry1.set_text("New PDML State Name")
		button2 = Gtk.Button(label="Save as New")
		button3 = Gtk.Button(label="Save Current")
		button4 = Gtk.Button(label="Close Current")
		button5 = Gtk.Button(label="Delete Current")
		entry6 = Gtk.Entry()
		entry6.set_text("Rename Current PDML State Name")
		button7 = Gtk.Button(label="Rename Current")

		menu.add(entry1)
		menu.attach_next_to(button2, entry1, 1, 1, 20)
		menu.attach_next_to(button3, button2, 1, 1, 20)
		menu.attach_next_to(button4, button3, 1, 1, 20)
		menu.attach_next_to(button5, button4, 1, 1, 20)
		menu.attach_next_to(entry6, button5, 1, 1, 20)
		menu.attach_next_to(button7, entry6, 1, 1, 20)

		vbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
		tbox = Gtk.Box(spacing = 2)

		label1 = Gtk.Label("Filter Area", xalign=0)
		label2 = Gtk.Label("Saved Filter")
		tbox.pack_start(label1, True, True, 0)
		entry = Gtk.Entry()
		entry.set_text("Filter Expression")
		vbox.pack_start(tbox, True, True, 0)
		vbox.pack_start(entry, True, True, 0)

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

		main_box.add(menu)
		main_box.attach_next_to(vbox, menu, Gtk.PositionType.BOTTOM, 1, 1)
		return main_box


win = mainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()


