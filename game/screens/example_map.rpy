screen example_map_screen: #Preparing the imagemap
    imagemap:
        ground "/screens/s_elements/map_city/city_map.jpg"
        hover "/screens/s_elements/map_city/city_map_hover.jpg"

        hotspot (540, 240, 120, 60) clicked Jump("home")
        hotspot (520, 375, 120, 60) clicked Jump("clinic")
 
label city_map_label:
call screen example_map_screen #Displaying the imagemap

label home:
    "It is Home."
    jump city_map_label

label clinic:
    "It is the clinic."
    jump city_map_label
