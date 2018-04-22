label test_sex_with_bar_screen_label:
scene bg img_player_map
if pc.energy < 1:
    "You are to tired have to go home"
    jump abstract_map_screen_label
else:
    "It is the public toilet"
    $pc.dec_energy(1)
    call screen test_sex_with_bar_screen

screen test_sex_with_bar_screen:

    if total % 2 == 1 :
        add "to_test_p1_1"
    elif total % 2 == 0:
        add "to_test_p1_2"
    vbox:
        style "action_screen_bar"
        bar:
            bar_vertical True
            value total
            range 5
            xysize(25,200)
        if total < 5:
            imagebutton auto "ab_suck_%s":
                action Function(incrementTotal)
        else:
            imagebutton auto "ab_suck_%s":
                action [Function(nullTotal), Jump("test_sex_with_bar_screen_label_2")]

label test_sex_with_bar_screen_label_2:
call screen test_sex_with_bar_screen_2

screen test_sex_with_bar_screen_2:
    if total % 2 == 1 :
        add "to_test_p2_1"
    elif total % 2 == 0:
        add "to_test_p2_2"
    vbox:
        style "action_screen_bar"
        bar:
            bar_vertical True
            value total
            range 5
            xysize(25,200)
        if total < 5:
            imagebutton auto "ab_take_%s":
                action Function(incrementTotal)
        else:
            imagebutton auto "ab_take_%s":
                action [Function(nullTotal), Jump("test_sex_with_bar_screen_label_3")]

label test_sex_with_bar_screen_label_3:
call screen test_sex_with_bar_screen_3

screen test_sex_with_bar_screen_3:
    if total % 2 == 1 :
        add "to_test_p3_1"
    elif total % 2 == 0:
        add "to_test_p3_2"
    vbox:
        style "action_screen_bar"
        bar:
            bar_vertical True
            value total
            range 5
            xysize(25,200)
        if total < 5:
            imagebutton auto "ab_enjoy_%s":
                action Function(incrementTotal)
        else:
            imagebutton auto "ab_enjoy_%s":
                action [Function(nullTotal), Jump("abstract_map_screen_label")]

label test_sex_with_bar_screen_end_label:
"LOGG test_sex_with_bar_screen_end_label"
