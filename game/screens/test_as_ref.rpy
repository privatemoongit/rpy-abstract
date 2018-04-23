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
    default ts = Sub_scene_variables()
    $ts.sub_scene_index_max_1 = 2
    $ts.sub_scene_index_max_2 = 3
    $ts.sub_scene_index_max_3 = 4
    call screen test_as

screen test_as:
    $pc.place = "test_as_reflabel"

    if ts.sub_scene_index_1 < ts.sub_scene_index_max_1:
        if ts.sub_scene_index_1 % 2 == 1 :
            add "to_test_p1_1"
        elif ts.sub_scene_index_1 % 2 == 0:
            add "to_test_p1_2"
        vbox:
            pos(1000,300)
            style "action_screen_bar"
            bar:
                bar_vertical True
                value ts.sub_scene_index_1
                range ts.sub_scene_index_max_1
                xysize(25,200)
            imagebutton auto "ab_enjoy_%s":
                action Function(ts.inc_sub_scene_index_1)
    elif ts.sub_scene_index_2 < ts.sub_scene_index_max_2:
        if ts.sub_scene_index_2 % 2 == 1 :
            add "to_test_p2_1"
        elif ts.sub_scene_index_2 % 2 == 0:
            add "to_test_p2_2"
        vbox:
            pos(100,300)
            style "action_screen_bar"
            bar:
                bar_vertical True
                value ts.sub_scene_index_2
                range ts.sub_scene_index_max_2
                xysize(25,200)
            imagebutton auto "ab_take_%s":
                action Function(ts.inc_sub_scene_index_2)
    elif ts.sub_scene_index_3 < ts.sub_scene_index_max_3:
        if ts.sub_scene_index_3 % 2 == 1 :
            add "to_test_p3_1"
        elif ts.sub_scene_index_3 % 2 == 0:
            add "to_test_p3_2"
        vbox:
            pos(1000,300)
            style "action_screen_bar"
            bar:
                bar_vertical True
                value ts.sub_scene_index_3
                range ts.sub_scene_index_max_3
                xysize(25,200)
            imagebutton auto "ab_enjoy_%s":
                action Function(ts.inc_sub_scene_index_3)
    else:
        if ts.sub_scene_index_3 % 2 == 1 :
            add "to_test_p3_1"
        elif ts.sub_scene_index_3 % 2 == 0:
            add "to_test_p3_2"
        imagebutton auto "cb_back_%s":
            action [Function(ts.null_sub_scene_index_1), Function(ts.null_sub_scene_index_2), Function(ts.null_sub_scene_index_3), Dissolve("test_as"), Jump("abstract_map_screen_label")]
            pos(1000,300)

    imagebutton:
        idle "mi_character_sheet_idle"
        hover "mi_character_sheet_hover"
        action [Dissolve("test_as"),Jump("player_character_sheet_screen_label")]
        pos(1200,50)
