label start:
    scene bg green
    "LOGG:script.rpy: begin"
#   call screen example_action_with_bar_screen
    jump abstract_map_screen_label
    label end_label:

    "LOGG:script.rpy: end_label [pc.place] [pc.energy]"
    return
