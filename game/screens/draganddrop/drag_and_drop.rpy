image bg dd_background = "to_test_p3_1"
image dd_map_icon_idle:
    "/images/icons/2hand.png"
    size(40,40)
image dd_map_icon_hovere:
    "dd_map_icon_idle"
    size(50,50)
image dd_ivy:
    "smartphone"
    size(40,40)
image dd_zack:
    "contacts"
    size(40,40)

image dd_london:
    "/consumable.png"
    size(55,55)
image dd_paris:
    "/square.png"
    size(55,55)
init python:

    def detective_dragged(drags, drop):

        if not drop:
            return

        store.detective = drags[0].drag_name
        store.city = drop.drag_name

        return True
label drag_and_drop_label:
jump send_detective
screen drag_and_drop_screen:
    add "dd_background"
    draggroup:
        # Our detectives.
        drag:
            drag_name "Ivy"
            child "dd_ivy"
            droppable False
            dragged detective_dragged
            xpos 100 ypos 100
        drag:
            drag_name "Zack"
            child "dd_zack"
            droppable False
            dragged detective_dragged
            xpos 150 ypos 100

        # The cities they can go to.
        drag:
            drag_name "London"
            child "dd_london"
            draggable False
            xpos 450 ypos 140
        drag:
            drag_name "Paris"
            draggable False
            child "dd_paris"
            xpos 500 ypos 280

    imagebutton:
        idle "mi_character_sheet_idle"
        hover "mi_character_sheet_hover"
        action [Dissolve("abstract_map_screen"), Call("drag_and_drop_screen")]
        pos(1200,50)

label send_detective:
    "We need to investigate! Who should we send, and where should they go?"

    call screen drag_and_drop_screen

    "Okay, we'll send [detective] to [city]."
    jump abstract_map_screen_label
