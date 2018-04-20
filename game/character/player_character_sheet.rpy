label player_character_sheet_screen_label:
call screen player_character_sheet_screen

screen player_character_sheet_screen:
    add "img_cs_background"
    vbox:
        xmaximum 300
        spacing 1
        label "Character Details" xalign 0.5
        grid pc.level 1:
            for i in range (0, pc.level):
                image "icon_cs_level"
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
        vbox:
            label "where am I : [pc.place]"
            image "icon_map_home_idle"

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

    imagebutton:
        idle "button_bar_idle"
        hover "button_bar_hover"
        pos(1100,600)
        action Jump(pc.place)
