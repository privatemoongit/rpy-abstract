default pc = Player()
image pie = "images/consumable.png"
defualt pie_item = Consumable("pie", 50, 100)

$inventory.append(pie_item)

label start:
    scene bg img_bluescreen_background
    "LOGG:script.rpy: begin"
#   call screen example_action_with_bar_screen
    jump abstract_map_screen_label
    label end_label:

    "LOGG:script.rpy: end_label [pc.place] [pc.energy]"
    return
