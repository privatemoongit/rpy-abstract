label journal_label:
call screen journal_screen
screen journal_screen:
    add "abstract_map"
    label "first journal entry"
    imagebutton:
        if pc.skillpoints > 0 :
            idle "mi_level_up_marker"
        else:
            idle "mi_character_sheet_idle"
        hover "mi_character_sheet_hover"
        action Jump("player_character_sheet_screen_label")
        pos(1200,50)
