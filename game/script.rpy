label start:
    scene bg green
    "LOGG:script.rpy: begin"
    #call screen player_character_sheet_screen
    jump abstract_map_screen_label
    label end_label:
    jump city_map_label

    "LOGG:script.rpy: end_label [pc.place] [pc.energy]"
    return
