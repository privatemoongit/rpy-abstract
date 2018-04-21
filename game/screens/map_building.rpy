label abstract_map_screen_label:
call screen abstract_map_screen

screen abstract_map_screen:
    $pc.changePlace("abstract_map_screen_label")
    image "img_player_map"

    vbox:
        hbox:
            label "energy:"
            for i in range (0, pc.energy):
                image "icon_cs_energie"
    imagebutton:
        idle "icon_cs_map_home_idle"
        hover "icon_cs_map_home_hover"
        action Jump("abstract_home")
        pos(540,240)
    imagebutton auto "images/icons/icons8-medical-doctor-64_%s.png":
        action Jump("abstract_clinic")
        pos(520,375)
#CHARACTER_SHEET
    imagebutton:
        idle "button_bar_idle"
        hover "button_bar_hover"
        action Jump("player_character_sheet_screen_label")
        pos(1200,50)

    imagebutton:
        idle "button_bar_idle"
        hover "button_bar_hover"
        action Jump("test_sex_with_bar_screen_label")
        pos(700,500)


label abstract_home:
    scene bg abstract_map
    "It is Home."
    jump end_label

label abstract_clinic:
    scene bg img_player_map
    if pc.energy < 1:
        "You are to tired have to go home"
        jump abstract_map_screen_label
    else:
        "It is the clinic"
        $pc.dec_energy(1)
        jump abstract_map_screen_label
