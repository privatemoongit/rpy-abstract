label abstract_map_screen_label:
call screen abstract_map_screen

screen abstract_map_screen:
    $pc.fromCH = False
    $pc.changePlace("home")
    image "abstract_map"

    vbox:
        bar:
            value pc.energy
            range pc.max_energy
            xysize(200, 25)

    imagebutton:
        idle "mi_home_idle"
        hover "mi_home_hover"
        action [Dissolve("abstract_map_screen"), Jump("home") ]
        pos(540,240)

    imagebutton:
        idle "mi_danjo_clinic_idle"
        hover "mi_danjo_clinic_hover"
        action [Function(pc.inc_exp_100), Jump("abstract_clinic")]
        pos(520,375)
    imagebutton:
        idle "mi_toilets_idle"
        hover "mi_toilets_hover"
        action [Dissolve("abstract_map_screen"), Jump("test_as_reflabel")]
        pos(200,400)
#CHARACTER_SHEET
    imagebutton:
        if pc.skillpoints > 0 :
            idle "mi_level_up_marker"
        else:
            idle "mi_character_sheet_idle"
        hover "mi_character_sheet_hover"
        action [Dissolve("abstract_map_screen"), Jump("player_character_sheet_screen_label")]
        pos(1200,50)

label home:
    scene bg abstract_map
    if "home" and pc.fromCH:
        jump abstract_map_screen_label
    "It is Home."
    jump end_label

label abstract_clinic:
    scene bg abstract_map
    if pc.energy < 1:
        "You are to tired have to go home"
        jump abstract_map_screen_label
    else:
        "It is the clinic"
        $pc.dec_energy(1)
        $pc.variant = "var_2"
        jump abstract_map_screen_label
