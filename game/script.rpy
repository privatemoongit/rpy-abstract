label start:
    scene bg green
    "LOGG:script.rpy: begin"
   # "LOGG:script.rpy: jump example_screen_script_screen"
   # jump example_screen_script_screen
    call screen example_map_screen
    label end_label:
    "LOGG:script.rpy: end_label"
    return
