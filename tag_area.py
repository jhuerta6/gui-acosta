import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class tag_area(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self,title="Tag Area")
        self.set_border_width(10)
        self.set_default_size(150,600)
        
        ## Main Container ##
        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=400)

        ## Sub Containers ##
        tag_box = Gtk.Grid()
        confirm_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=4)
        main_box.pack_start(tag_box, True, True, 0)
        main_box.pack_start(confirm_box, True, True, 0)

        self.add(main_box)

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


win = tag_area()
win.connect("destroy",Gtk.main_quit)
win.show_all()
Gtk.main()
