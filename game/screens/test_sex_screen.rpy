label test_sex_with_bar_screen_label:
scene bg abstract_map
if pc.energy < 1:
    "You are to tired have to go home"
    jump abstract_map_screen_label
else:
    "It is the public toilet"
    $pc.dec_energy(1)
    call screen test_sex_with_bar_screen

label test_sex_with_bar_screen_label_2:
call screen test_sex_with_bar_screen_2

label test_sex_with_bar_screen_label_3:
call screen test_sex_with_bar_screen_3

screen test_sex_with_bar_screen:
    $pc.place = "test_sex_with_bar_screen_label"

    if sub_scene_index_1 % 2 == 1 :
        add "to_test_p1_1"
    elif sub_scene_index_1 % 2 == 0:
        add "to_test_p1_2"
    vbox:
        pos(1000,300)
        style "action_screen_bar"
        bar:
            bar_vertical True
            value sub_scene_index_1
            range sub_scene_index_max_1
            xysize(25,200)
        if sub_scene_index_1 < sub_scene_index_max_1:
            imagebutton auto "ab_suck_%s":
                action Function(inc_sub_index_1)
        else :
            imagebutton auto "ab_suck_%s":
                action [Function(null_sub_index_1), Jump("test_sex_with_bar_screen_label_2")]

screen test_sex_with_bar_screen_2:
    if sub_scene_index_2 % 2 == 1 :
        add "to_test_p2_1"
    elif sub_scene_index_2 % 2 == 0:
        add "to_test_p2_2"
    vbox:
        style "action_screen_bar"
        bar:
            bar_vertical True
            value sub_scene_index_2
            range sub_scene_index_max_2
            xysize(25,200)
        if sub_scene_index_2 < sub_scene_index_max_2:
            imagebutton auto "ab_take_%s":
                action Function(inc_sub_index_2)
        else:
            imagebutton auto "ab_take_%s":
                action [Function(null_sub_index_2), Jump("test_sex_with_bar_screen_label_3")]

screen test_sex_with_bar_screen_3:
    if sub_scene_index_3 % 2 == 1 :
        add "to_test_p3_1"
    elif sub_scene_index_3 % 2 == 0:
        add "to_test_p3_2"
    vbox:
        style "action_screen_bar"
        bar:
            bar_vertical True
            value sub_scene_index_3
            range sub_scene_index_max_3
            xysize(25,200)
        if sub_scene_index_3 < sub_scene_index_max_3:
            imagebutton auto "ab_enjoy_%s":
                action Function(inc_sub_index_3)
        else:
            imagebutton auto "ab_enjoy_%s":
                action [Function(null_sub_index_3), Jump("abstract_map_screen_label")]

label test_sex_with_bar_screen_end_label:
"LOGG test_sex_with_bar_screen_end_label"
