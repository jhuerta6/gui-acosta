import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

field = [("icmp.type", "Type 8 [Echo [ping] request", 1, 34, 8, 8, 2),
         ("icmp.code", "Code 0", 1, 35, 0, 0, 2), ("icmp.checksum", "Checksum: 0x6861 [correct]", 0, 36, 24, 6861, 0)]



def create_pdml_view():

    
    main_container = Gtk.Grid()

    ## Top section of PDML View ##
    
    pdml_menu_grid = Gtk.Grid()
    
    new_name_pdml = Gtk.Entry()
    new_name_pdml.set_text("New PDML State Name")
    save_new_button = Gtk.Button.new_with_label("Save as New PDML State")
    save_curr_button = Gtk.Button.new_with_label("Save Current PDML State")
    close_curr_button = Gtk.Button.new_with_label("Close Current PDML State")
    delete_curr_button = Gtk.Button.new_with_label("Delete Current PDML State")
    rename_pdml = Gtk.Entry()
    rename_pdml.set_text("Rename Current PDML State Name")
    rename_curr_button = Gtk.Button.new_with_label("Rename Current PDML State")

    pdml_menu_grid.attach(new_name_pdml,0,0,2,1)
    pdml_menu_grid.attach(save_new_button,1,0,1,1)
    pdml_menu_grid.attach(save_curr_button,2,0,1,1)
    pdml_menu_grid.attach(close_curr_button,3,0,1,1)
    pdml_menu_grid.attach(delete_curr_button,4,0,1,1)
    pdml_menu_grid.attach(rename_pdml,5,0,2,1)
    pdml_menu_grid.attach(rename_curr_button,6,0,1,1)

    ## Filter Area ##
    vbox_filterarea = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    tbox = Gtk.Box(spacing = 2)

    label1 = Gtk.Label("Filter Area", xalign=0)
    label2 = Gtk.Label("Saved Filter")
    tbox.pack_start(label1, True, True, 0)
    entry = Gtk.Entry()
    entry.set_text("Filter Expression")
    vbox_filterarea.pack_start(tbox, True, True, 0)
    vbox_filterarea.pack_start(entry, True, True, 0)
    
    applyBut = Gtk.Button(label="Apply")
    clearBut = Gtk.Button(label="Clear")
    saveBut = Gtk.Button(label="Save")
    saveFilters = Gtk.ComboBox()
    applyFil = Gtk.Button(label="Apply")

    vbox_filterarea.pack_start(applyBut, True, True, 0)
    vbox_filterarea.pack_start(clearBut, True, True, 0 )
    vbox_filterarea.pack_start(saveBut, True, True, 0)
    vbox_filterarea.pack_start(label2, True, True, 0)
    vbox_filterarea.pack_start(saveFilters, True, True, 0)
    vbox_filterarea.pack_start(applyFil, True, True, 0)

    ## Field Area ##
    ## NEED TO POPULATE WITH FIELD DATA FROM THE PDML FILE
    ## CURRENTLY BEING HARD CODED WITH 'field' LIST FROM BEGINNING OF THE FILE

    field_area = Gtk.Box()

    fieldstore = Gtk.ListStore(str,str,int,int,int,int,int)

    for item in field: ## Need to fill 'field' with pdml info!! ##
        fieldstore.append(list(item))
    fieldview = Gtk.TreeView(fieldstore)


    for i, coltitle in enumerate(["Field Name", "Showname", "Size", "Position", "Show", "Value", "Entropy"]):

        render = Gtk.CellRendererText()

        column = Gtk.TreeViewColumn(coltitle, render, text=i)

        fieldview.append_column(column)

    field_area.pack_start(fieldview, True, True, 0)

    ## Message Type Area
    type_area_notebook = Gtk.Notebook()
    page1 = Gtk.Grid()
    page1.set_border_width(10)
    mTypeGuide = Gtk.Label("To create a new message type, please enter a message type name and select message type field value pair(s). \nTo update/delete an existing message type, please select from the existing message type, please select from \nthe existing message type first and the previously selected name and field value pair(s) will be pre-populated.")
    mTypeGuide.set_line_wrap(True)
    existingTypeLabel = Gtk.Label("Existing Message Type")
    mTypeName = Gtk.Label("Message Type Name")
    fieldValueLabel = Gtk.Label("Message Type Field Value Pairs")
    existingTypeBox = Gtk.ComboBox()
    mTypeEntry = Gtk.Entry()
    fieldValuePairs = Gtk.Entry()
    deleteBut = Gtk.Button(label="Delete")
    saveBut = Gtk.Button(label="Save")
    clearBut = Gtk.Button(label="Clear")
    check1 = Gtk.CheckButton.new_with_label("Select both field name and value")
    check2 = Gtk.CheckButton.new_with_label("Select field name only")
    page1.attach(mTypeGuide, 0, 0, 2, 2)
    page1.attach(existingTypeLabel, 0, 2, 1, 1)
    page1.attach(existingTypeBox, 1, 2, 1, 1)
    page1.attach(mTypeName, 0, 3, 1, 1)
    page1.attach(mTypeEntry, 1, 3, 1, 1)
    page1.attach(fieldValueLabel,  0, 4, 1, 1)
    page1.attach(fieldValuePairs, 1, 4, 1, 1)
    page1.attach(check1, 0, 5, 1, 1)
    page1.attach(check2, 0, 6, 1, 1)
    page1.attach(deleteBut, 0, 7, 1, 1)
    page1.attach(saveBut, 1, 7, 1, 1)
    page1.attach(clearBut, 2, 7, 1, 1)
    type_area_notebook.append_page(page1, Gtk.Label('New/Modify'))


    page2 = Gtk.Box()
    page2.set_border_width(10)
    page2.add(Gtk.Label('Under Construction.'))
    type_area_notebook.append_page(page2, Gtk.Label('Dependency'))

    page3 = Gtk.Box()
    page3.set_border_width(10)
    page3.add(Gtk.Label('Under Construction'))
    type_area_notebook.append_page(page3, Gtk.Label('Template'))

    page4 = Gtk.Box()
    page4.set_border_width(10)
    page4.add(Gtk.Label('Under Construction'))
    type_area_notebook.append_page(page4, Gtk.Label('Equivalency'))

    page5 = Gtk.Box()
    page5.set_border_width(10)
    page5.add(Gtk.Label('Under Construction'))
    type_area_notebook.append_page(page5, Gtk.Label('Generation'))

    ## Add to main container ##

    main_container.add(pdml_menu_grid)
    main_container.attach(vbox_filterarea,0,1,2,1)
    main_container.attach(field_area,0,3,1,1)
    main_container.attach(type_area_notebook,1,3,1,1)
    

    return main_container
