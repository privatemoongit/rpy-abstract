default pc = Player()
image pie = "images/consumable.png"
default pie_item = Consumable("pie", "pie", 1, 1)
default selected_item = Consumable("square", "", 0, 0)
image square = "images/square.png"
style slot:
    background Frame("square", 0, 0)
    minimum(75,75)
    maximum(75,75)
    xalign 0.5



label start:
    #scene bg img_bluescreen_background
    #"LOGG:script.rpy: begin"
#   call screen example_action_with_bar_screen
    #jump abstract_map_screen_label
    $pc.add_item(pie_item)
    "[pc.inventory]"
    jump player_character_sheet_screen_label
    label end_label:

    "LOGG:script.rpy: end_label [pc.place] [pc.energy]"
    return
