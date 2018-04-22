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
        action Jump("home")
        pos(540,240)

    imagebutton:
        idle "mi_danjo_clinic_idle"
        hover "mi_danjo_clinic_hover"
        action Jump("abstract_clinic")
        pos(520,375)
    imagebutton:
        idle "mi_toilets_idle"
        hover "mi_toilets_hover"
        action Jump("test_sex_with_bar_screen_label")
        pos(700,500)

#CHARACTER_SHEET
    imagebutton:
        idle "mi_character_sheet_idle"
        hover "mi_character_sheet_hover"
        action Jump("player_character_sheet_screen_label")
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
        jump abstract_map_screen_label
