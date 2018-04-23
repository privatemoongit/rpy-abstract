label test_as_reflabel:
scene bg abstract_map
#Check if pc comming back from the ch
if pc.from_cs:
    call screen test_as
#check if the pchave the energy to perform the scene
elif pc.energy < 1:
    "You are to tired have to go home"
    jump abstract_map_screen_label
#proceed to the scene
else:
    "It is the public toilet"
    $pc.dec_energy(1)
    #check if the pc have the skill to modify the scene and offer choise to pc
    #to do if wishes
    if pc.sxskills > 0:
        menu:
            "Inc":
                jump inc_label
            "Dec":
                jump dec_label
            "Def":
                jump def_label
    #defining the scene variables
    default ts = Sub_scene_variables()
    label inc_label:
        $ts.sub_scene_index_max_1 = 2 + pc.sxskills
        $ts.sub_scene_index_max_2 = 3 + pc.sxskills
        $ts.sub_scene_index_max_3 = 4 + pc.sxskills
        call screen test_as

    label dec_label:
        $ts.sub_scene_index_max_1 = 2 - pc.sxskills
        $ts.sub_scene_index_max_2 = 3 - pc.sxskills
        $ts.sub_scene_index_max_3 = 4 - pc.sxskills
        call screen test_as

    label def_label:
        $ts.sub_scene_index_max_1 = 2
        $ts.sub_scene_index_max_2 = 3
        $ts.sub_scene_index_max_3 = 4
        call screen test_as

screen test_as:
    #changing the place of pc if needed
    $pc.place = "test_as_reflabel"

    if ts.sub_scene_index_1 < ts.sub_scene_index_max_1:
        if ts.sub_scene_index_1 % 2 == 1 :
            add "to_test_p1_1"
        elif ts.sub_scene_index_1 % 2 == 0:
            add "to_test_p1_2"
        vbox:
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
            style "action_screen_bar"
            bar:
                bar_vertical True
                value ts.sub_scene_index_2
                range ts.sub_scene_index_max_2
                xysize(25,200)
            imagebutton auto "ab_take_%s":
                action Function(ts.inc_sub_scene_index_2)
        #extra thing pc is allowed to do during the scene
        if ts.sub_scene_index_2 > 1:
            imagebutton auto "ab_take_%s":
                action [Jump("sub_scene_index_2_sub_label")]
                pos(1200,50)
    elif ts.sub_scene_index_3 < ts.sub_scene_index_max_3:
        if ts.sub_scene_index_3 % 2 == 1 :
            add "to_test_p3_1"
        elif ts.sub_scene_index_3 % 2 == 0:
            add "to_test_p3_2"
        vbox:
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
        #end of the screen clean up
        imagebutton auto "cb_back_%s":
            action [Function(ts.null_sub_scene_index_1), Function(ts.null_sub_scene_index_2), Function(ts.null_sub_scene_index_3), Dissolve("test_as"), Jump("abstract_map_screen_label")]
            pos(1000,300)
    #check the pcsheet during an action screen
    imagebutton:
        idle "mi_character_sheet_idle"
        hover "mi_character_sheet_hover"
        action [Dissolve("test_as"),Jump("player_character_sheet_screen_label")]
        pos(1200,50)

#extra thing what pc is allowed to do impl
label sub_scene_index_2_sub_label:
call screen sub_scene_index_2_sub_screen
screen sub_scene_index_2_sub_screen:
    $pc.from_cs = True
    image "abstract_map"
    vbox:
        pos(600,350)
        label "[ts.sub_scene_index_1]"
        label "[ts.sub_scene_index_2]"
    #jumping back to scene where the player was after the extra thing
    imagebutton auto "ab_take_%s":
        action Jump(pc.place)
        pos(1200,50)
