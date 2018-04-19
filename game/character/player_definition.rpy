init python:
    class Player:
        def __init__(self, level, experiance, energy, willpower, morals, money):
            self.level = level
            self.experiance = experiance
            self.energy = energy
            self.max_energy = energy
            self.willpower = willpower
            self.morals = morals
            self.money = money
            self.place = "home"

        def getPlace(self):
            return self.place
        def changePlace(self, place):
            self.place = place

        def levelUp(self):
            self.incMaxEnergy()

        def incExperiance(self, ammount):
            self.experiance += ammount
            if (self.checkLevelUp()):
                self.level += 1
                self.levelUp()

        def incMaxEnergy(self):
            self.max_energy += 1

        def reEnergy(self, ammount):
            if self.max_energy - self.energy - ammount >= 0:
                self.energy += ammount
            else:
                self.energy = self.max_energy

        def decEnergy(self, ammount):
            self.energy -= ammount
            if self.energy > 0:
                return True
            else:
                self.energy = 0
                return False

        def decWillpower(self, ammount):
            self.willpower -= ammount

        def incWillpower(self, ammount):
            self.willpower += ammount

        def decMoral(self, ammount):
            self.morals -= ammount

        def incMoral(self, ammount):
            self.morals += ammount

        def incMoney(self, ammount):
            self.money += ammount

        def decMoney(self, ammount):
            if self.money - ammount >= 0:
                self.money -= ammount
                return True
            else:
                return False

        def checkLevelUp(self):
            if(self.experiance) > 100 and self.level <= 1:
                return True
            elif(self.experiance) > 200 and self.level <= 2:
                return True
            elif(self.experiance) > 400 and self.level <= 3:
                return True
            elif(self.experiance) > 800 and self.level <= 4:
                return True
            elif(self.experiance) > 1600 and self.level <= 5:
                return True
            elif(self.experiance) > 3200 and self.level <= 6:
                return True
            elif(self.experiance) > 6400 and self.level <= 7:
                return True
            elif(self.experiance) > 12800 and self.level <= 8:
                return True
            elif(self.experiance) > 25600 and self.level <= 9:
                return True
            elif(self.experiance) > 51200 and self.level <= 10:
                return True
