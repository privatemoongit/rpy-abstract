label player_character_sheet_screen_label:
call screen player_character_sheet_screen
screen player_character_sheet_screen:
    add "screens/s_elements/action_with_bar/backgrounds/bg_bluescreen.jpg"
    vbox:
        xmaximum 300
        spacing 2
        label "Character Details" xalign 0.5
        grid pc.level 1:
            for i in range (0, pc.level):
                image "/screens/s_elements/action_with_bar/buttons/button_selected_idle.png"
        label "level: [pc.level]"
        label "experiance: [pc.experiance] / 100"
        hbox:
            label "energy: [pc.energy] / [pc.max_energy]"
            if pc.skillpoints > 0 :
                textbutton "+" action Function(pc.inc_max_energy)
        hbox:
            label "willpower: [pc.willpower]"
            if pc.skillpoints > 0 :
                textbutton "+" action Function(pc.inc_willpower)

        label "morals: [pc.morals]"
        if is_woman :
            label "histeria: [pc.histeria]"

        label "money: [pc.money]"
        label "where am I : [pc.place]"

        label "Skills: "
        label "skillpoints: [pc.skillpoints]"
        hbox:
            label "computers [pc.computers]"
            if pc.skillpoints > 0 :
                textbutton "+" action Function(pc.inc_computers)
        hbox:
            label "fittness [pc.fittness]"
            if pc.skillpoints > 0 :
                textbutton "+" action Function(pc.inc_fittness)
        hbox:
            label "security [pc.security]"
            if pc.skillpoints > 0 :
                textbutton "+" action Function(pc.inc_security)
        hbox:
            label "sxskills [pc.sxskills]"
            if pc.skillpoints > 0 :
                textbutton "+" action Function(pc.inc_sxskills)
        hbox:
            label "sneak [pc.sneak]"
            if pc.skillpoints > 0 :
                textbutton "+" action Function(pc.inc_sneak)
        hbox:
            label "speech [pc.speech]"
            if pc.skillpoints > 0 :
                textbutton "+" action Function(pc.inc_speech)
        hbox:
            label "speech [pc.place]"

        if pc.place == "city_map_label":
            textbutton "Return":
                xalign 05
                yalign 0.95
                action Jump("city_map_label")
        else:
            textbutton "Return":
                xalign 05
                yalign 0.95
                action Return()
