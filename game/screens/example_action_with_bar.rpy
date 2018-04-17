style centered_style:
    xalign 0.5
    yalign 0.5

style centered_param_style is centered_style:
    spacing 10
    xmaximum 300
    box_wrap True

define total = 0
init python:
    def incrementTotal():
        global total
        total+=1
    def nullTotal():
        global total
        total = 0


screen example_action_with_bar_screen:
    if total % 2 == 1 :
        add "screens/s_elements/action_with_bar/backgrounds/bg_bluescreen.jpg"
    elif total % 2 == 0:
        add "screens/s_elements/action_with_bar/backgrounds/bg_greenscreen.jpg"
    bar:
        xalign 0.5
        yalign 0.5
        bar_vertical True
        value total
        range 10
        xysize(25,200)
    if total < 10:
        imagebutton auto "/screens/s_elements/action_with_bar/buttons/button_%s.png":
            action Function(incrementTotal)
    else:
        imagebutton auto "/screens/s_elements/action_with_bar/buttons/button_%s.png":
            action Null
