screen example_action_with_bar_screen:
    if total % 2 == 1 :
        add "img_bluescreen_background"
    elif total % 2 == 0:
        add "img_greencreen_background"
    hbox:
        style "action_screen_bar"
        bar:
            bar_vertical True
            value total
            range 4
            xysize(25,200)
        if total < 5:
            imagebutton:
                idle "ai_bar_button_idle"
                hover "ai_bar_button_hover"
                action Function(incrementTotal)
        else:
            imagebutton:
                idle "button_bar_idle"
                hover "button_bar_hover"
                action Jump("example_action_with_bar_screen_end_label")

label example_action_with_bar_screen_end_label:
"LOGG example_action_with_bar_screen_end_label"
