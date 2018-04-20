image bg abstract_map = "/images/map/player_map.png"

screen abstract_map_screen: #Preparing the imagemap
    $pc.changePlace("abstract_map_screen_label")
    image "/images/map/player_map.png"

    vbox:
        hbox:
            label "energy:"
            for i in range (0, pc.energy):
                image "/screens/s_elements/action_with_bar/buttons/button_selected_idle.png"
    imagebutton auto "images/icons/icons8-home-24_%s.png":
        action Jump("abstract_home")
        pos(540,240)
    imagebutton auto "images/icons/icons8-medical-doctor-64_%s.png":
        action Jump("abstract_clinic")
        pos(520,375)
    imagebutton auto "/screens/s_elements/action_with_bar/buttons/button_selected_%s.png":
        action Jump("player_character_sheet_screen_label")
        pos(1200,50)
label abstract_map_screen_label:
call screen abstract_map_screen #Displaying the imagemap

#scene bg background_map
label abstract_home:
    scene bg abstract_map
    $pc.changePlace("abstract_home")
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
        $pc.changePlace("abstract_clinic")
        jump abstract_map_screen_label
