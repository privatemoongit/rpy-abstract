screen player_character_sheet_screen:
    add "screens/s_elements/action_with_bar/backgrounds/bg_bluescreen.jpg"
    vbox:
        xmaximum 300
        spacing 2
        label "Character Details" xalign 0.5
        grid pc.level 1:
            for i in range (0, pc.level):
                imagebutton auto "/screens/s_elements/action_with_bar/buttons/button_selected_%s.png":
                    action Null
        label "level: [pc.level]"
        label "experiance: [pc.experiance]"
        label "energy: [pc.energy] / [pc.max_energy]"
        label "willpower: [pc.willpower]"
        label "morals: [pc.morals]"
        label "money: [pc.money]"
        label "where am I : [pc.place]"

    textbutton "Return":
        action Return()
        xalign 05
        yalign 0.95
