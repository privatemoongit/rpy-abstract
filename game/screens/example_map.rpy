image bg background_map = "/screens/s_elements/map_city/city_map.jpg"

screen example_map_screen: #Preparing the imagemap
    imagemap:
        ground "/screens/s_elements/map_city/city_map.jpg"
        hover "/screens/s_elements/map_city/city_map_hover.jpg"

        hotspot (540, 240, 120, 60) clicked Jump("home")
        hotspot (520, 375, 120, 60) clicked Jump("clinic")
    hbox:
        for i in range (0, pc.energy):
            image "/screens/s_elements/action_with_bar/buttons/button_selected_idle.png"
label city_map_label:
call screen example_map_screen #Displaying the imagemap

#scene bg background_map
label home:
    scene bg background_map
    $pc.changePlace("home")
    "It is Home."
    jump end_label

label clinic:
    scene bg background_map
    if pc.energy < 1:
        "You are to tired have to go home"
        jump city_map_label
    else:
        "It is the clinic"
        $pc.decEnergy(1)
        $pc.changePlace("clinic")
        jump city_map_label
