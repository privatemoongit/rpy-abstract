define total = 0
define total_2 = 0

define sub_scene_index_1 = 0
define sub_scene_index_2 = 0
define sub_scene_index_3 = 0
define sub_scene_index_4 = 0
define sub_scene_index_5 = 0

define sub_scene_index_max_1 = 2
define sub_scene_index_max_2 = 5
define sub_scene_index_max_3 = 7
define sub_scene_index_max_4 = 5
define sub_scene_index_max_5 = 5

define is_sub_scene_finished = False
define is_scene_finished = False

define is_woman = False
define from_to_charsheet = 0

init python:
    class sub_scene_variables:
        def __init__(self):
            self.sub_scene_index_1 = 0
            self.sub_scene_index_2 = 0
            self.sub_scene_index_3 = 0
            self.sub_scene_index_4 = 0
            self.sub_scene_index_5 = 0
