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
    class Sub_scene_variables:
        def __init__(self):
            self.sub_scene_index_1 = 0
            self.sub_scene_index_2 = 0
            self.sub_scene_index_3 = 0
            self.sub_scene_index_4 = 0
            self.sub_scene_index_5 = 0

            self.sub_scene_index_max_1 = 0
            self.sub_scene_index_max_2 = 0
            self.sub_scene_index_max_3 = 0
            self.sub_scene_index_max_4 = 0
            self.sub_scene_index_max_5 = 0

        def inc_sub_scene_index_1(self):
            self.sub_scene_index_1 += 1
        def null_sub_scene_index_1(self):
            self.sub_scene_index_1 -= self.sub_scene_index_1

        def inc_sub_scene_index_2(self):
            self.sub_scene_index_2 += 1
        def null_sub_scene_index_2(self):
            self.sub_scene_index_2 -= self.sub_scene_index_2

        def inc_sub_scene_index_3(self):
            self.sub_scene_index_3 += 1
        def null_sub_scene_index_3(self):
            self.sub_scene_index_3 -= self.sub_scene_index_3

        def inc_sub_scene_index_4(self):
            self.sub_scene_index_4 += 1
        def null_sub_scene_index_4(self):
            self.sub_scene_index_4 -= self.sub_scene_index_4

        def inc_sub_scene_index_5(self):
            self.sub_scene_index_5 += 1
        def null_sub_scene_index_5(self):
            self.sub_scene_index_5 -= self.sub_scene_index_5
