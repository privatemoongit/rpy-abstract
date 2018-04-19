screen example_action_with_bar_screen:
    if total % 2 == 1 :
        add "screens/s_elements/action_with_bar/backgrounds/bg_bluescreen.jpg"
    elif total % 2 == 0:
        add "screens/s_elements/action_with_bar/backgrounds/bg_greenscreen.jpg"
    hbox:
        style "action_screen_bar"
        bar:
            bar_vertical True
            value total
            range 4
            xysize(25,200)
        if total < 5:
            imagebutton auto "/screens/s_elements/action_with_bar/buttons/button_%s.png":
                action Function(incrementTotal)
        else:
            imagebutton auto "/screens/s_elements/action_with_bar/buttons/button_selected_%s.png":
                action Jump("example_action_with_bar_screen_end_label")

label example_action_with_bar_screen_end_label:
"LOGG example_action_with_bar_screen_end_label"
