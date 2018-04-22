label abstract_map_screen_label:
call screen abstract_map_screen

screen abstract_map_screen:
    $pc.changePlace("abstract_map_screen_label")
    image "abstract_map"

    vbox:
        hbox:
            label "energy:"
            for i in range (0, pc.energy):
                image "ci_energy_idle"
    imagebutton:
        idle "mi_home_idle"
        hover "mi_home_hover"
        action Jump("abstract_home")
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



label abstract_home:
    scene bg abstract_map
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
