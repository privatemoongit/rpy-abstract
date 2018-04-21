init python:
    class Player:
        default_level = 1
        default_experiance = 200
        default_energy = 3
        default_willpower = 1
        default_morals = 5
        default_histeria = 0

        default_money = 300
        default_place = "abstract_map_screen_label"
        default_inventory = []

        default_skillpoints = 2

        default_computers = 1
        default_fittness = 0
        default_sxskill = 0
        default_security = 0
        default_sneak = 0
        default_speech = 0

        def __init__(self):
            self.init_atributes()
            self.init_baiscs()
            self.init_skills()

        def init_atributes(self):
            self.level = self.default_level
            self.experiance = self.default_experiance
            self.energy = self.default_energy
            self.max_energy = self.energy
            self.willpower = self.default_willpower
            self.morals = self.default_morals
            self.histeria = self.default_histeria

        def init_baiscs(self):
            self.money = self.default_money
            self.place = self.default_place
            self.inventory = self.default_inventory

        def init_skills(self):
            self.skillpoints = self.default_skillpoints
            self.computers = self.default_computers
            self.fittness = self.default_fittness
            self.sxskills = self.default_sxskill
            self.security = self.default_security
            self.sneak = self.default_sneak
            self.speech = self.default_speech

        def getPlace(self):
            return self.place

        def changePlace(self, place):
            self.place = place

        def level_up(self):
            self.max_energy += 1
            self.inc_skillpoints()

        def inc_experiance(self, ammount):
            self.experiance += ammount
            while self.experiance >= 100:
                self.level += 1
                self.level_up()
                self.experiance -= 100

        def inc_max_energy(self):
            if self.skillpoints > 0 :
                self.skillpoints-=1
                self.max_energy +=1

        def inc_skillpoints(self):
            self.skillpoints += 1

        def inc_computers(self):
            if self.skillpoints > 0 :
                self.skillpoints-=1
                self.computers +=1

        def inc_fittness(self):
            if self.skillpoints > 0 :
                self.skillpoints-=1
                self.fittness +=1

        def inc_sxskills(self):
            if self.skillpoints > 0 :
                self.skillpoints-=1
                self.sxskills +=1

        def inc_security(self):
            if self.skillpoints > 0 :
                self.skillpoints-=1
                self.security +=1

        def inc_sneak(self):
            if self.skillpoints > 0 :
                self.skillpoints-=1
                self.sneak +=1

        def inc_speech(self):
            if self.skillpoints > 0 :
                self.skillpoints-=1
                self.speech +=1

        def re_energy(self, ammount):
            if self.max_energy - self.energy - ammount >= 0:
                self.energy += ammount
            else:
                self.energy = self.max_energy

        def dec_energy(self, ammount):
            self.energy -= ammount
            if self.energy > 0:
                return True
            else:
                self.energy = 0
                return False

        def dec_willpower(self, ammount):
            self.willpower -= ammount

        def inc_willpower(self):
            if self.skillpoints > 0 :
                self.skillpoints-=1
                self.willpower +=1


        def dec_moral(self, ammount):
            self.morals -= ammount

        def inc_moral(self, ammount):
            self.morals += ammount

        def dec_histeria(self, ammount):
            self.histeria -= ammount

        def inc_histeria(self, ammount):
            self.histeria += ammount

        def inc_money(self, ammount):
            self.money += ammount

        def dec_money(self, ammount):
            if self.money - ammount >= 0:
                self.money -= ammount
                return True
            else:
                return False

    class Consumable:
        def __init__(self, img, name, ammount):
            self.img = img
            self.name = name
            self.ammount = ammount

        def use(self, target):
            target.inventory.remove(self)
            target.re_energy(self.ammount)
            #global selected_item
            #selected_item = None
