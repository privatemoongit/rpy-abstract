label test_as_reflabel:
scene bg abstract_map
if pc.fromCH:
    call screen test_as
elif pc.energy < 1:
    "You are to tired have to go home"
    jump abstract_map_screen_label
else:
    "It is the public toilet"
    $pc.dec_energy(1)
    call screen test_as

screen test_as:
    $pc.place = "test_as_reflabel"

    if sub_scene_index_1 < sub_scene_index_max_1:
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
            imagebutton auto "ab_enjoy_%s":
                action Function(inc_sub_index_1)
    elif sub_scene_index_2 < sub_scene_index_max_2:
        if sub_scene_index_2 % 2 == 1 :
            add "to_test_p2_1"
        elif sub_scene_index_2 % 2 == 0:
            add "to_test_p2_2"
        vbox:
            pos(100,300)
            style "action_screen_bar"
            bar:
                bar_vertical True
                value sub_scene_index_2
                range sub_scene_index_max_2
                xysize(25,200)
            imagebutton auto "ab_take_%s":
                action Function(inc_sub_index_2)
    elif sub_scene_index_3 < sub_scene_index_max_3:
        if sub_scene_index_3 % 2 == 1 :
            add "to_test_p3_1"
        elif sub_scene_index_3 % 2 == 0:
            add "to_test_p3_2"
        vbox:
            pos(1000,300)
            style "action_screen_bar"
            bar:
                bar_vertical True
                value sub_scene_index_3
                range sub_scene_index_max_3
                xysize(25,200)
            imagebutton auto "ab_enjoy_%s":
                action Function(inc_sub_index_3)
    else:
        if sub_scene_index_3 % 2 == 1 :
            add "to_test_p3_1"
        elif sub_scene_index_3 % 2 == 0:
            add "to_test_p3_2"
        imagebutton auto "cb_back_%s":
            action [Function(null_sub_index_1), Function(null_sub_index_2), Function(null_sub_index_3), Dissolve("test_as"), Jump("abstract_map_screen_label")]
            pos(1000,300)

    imagebutton:
        idle "mi_character_sheet_idle"
        hover "mi_character_sheet_hover"
        action [Dissolve("test_as"),Jump("player_character_sheet_screen_label")]
        pos(1200,50)
