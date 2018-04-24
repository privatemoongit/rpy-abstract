default inventory = []
default selected_item = None
image pie = "images/consumable.png"

$ pie_item = Consumable("pie", 50, 100)
$inventory.append(pie_item)

style slot:
    background Frame("square", 0, 0)
    minimum(80,80)
    maximum(80,80)
    xalign 0.5

label player_character_sheet_screen_label:
call screen player_character_sheet_screen

screen player_character_sheet_screen:
    $pc.from_cs = True
    add "img_character_sheet_dna_bg"
    image "[pc.variant]":
        pos(50,20)
        size(225,225)
    vbox:
        pos(295,20)
        xmaximum 500
        hbox:
            textbutton "level: [pc.level]"
            textbutton "experiance: [pc.experiance] / 100"
        hbox:
            bar:
                value pc.energy
                range pc.max_energy
                xysize(200, 25)
            textbutton "  ([pc.energy] / [pc.max_energy])"
            if pc.skillpoints > 0 and pc.place == "home":
                textbutton "+" action Function(pc.inc_max_energy)
        textbutton "morals: [pc.morals]"
        textbutton "histeria: [pc.histeria]"
        hbox:
            textbutton "willpower: [pc.willpower]"
            if pc.skillpoints > 0 and pc.place == "home":
                textbutton "+" action Function(pc.inc_willpower)
        textbutton "money: [pc.money]"
        textbutton "current place: [pc.place]"
    vbox:
        pos(650, 20)
        textbutton "Skills / skillpoints to spent: [pc.skillpoints]"

        hbox:
            textbutton "computers [pc.computers]"
            if pc.skillpoints > 0 and pc.place == "home":
                textbutton "+" action Function(pc.inc_fittness)
        hbox:
            textbutton "fittness [pc.fittness]"
            if pc.skillpoints > 0 and pc.place == "home":
                textbutton "+" action Function(pc.inc_fittness)
        hbox:
            textbutton "security [pc.security]"
            if pc.skillpoints > 0 and pc.place == "home":
                textbutton "+" action Function(pc.inc_security)
        hbox:
            textbutton "sxskills [pc.sxskills]"
            if pc.skillpoints > 0 and pc.place == "home":
                textbutton "+" action Function(pc.inc_sxskills)
        hbox:
            textbutton "sneak [pc.sneak]"
            if pc.skillpoints > 0 and pc.place == "home":
                textbutton "+" action Function(pc.inc_sneak)
        hbox:
            textbutton "speech [pc.speech]"
            if pc.skillpoints > 0 and pc.place == "home":
                textbutton "+" action Function(pc.inc_speech)
    hbox:
        pos(1160, 20)
        spacing 20
        imagebutton:
            idle "microblog"
            action Jump("journal_label")
        imagebutton:
            idle  "contacts"
            action Jump("contacts_label")
#INVENTORY
    grid 5 5:
        pos(20, 300)
        spacing 5
        for item in inventory:
            frame:
                style "slot"
                imagebutton idle item.img action SetVariable("selected_item", item)
        for i in range(len(inventory), 25):
            frame:
                style "slot"


    imagebutton auto "cb_back_%s":
        pos(1100,600)
        action [Dissolve("player_character_sheet_screen"),Jump(pc.place)]
