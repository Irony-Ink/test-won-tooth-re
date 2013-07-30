###################
#Program: Dice tests
#Author: BabyMaybe
#Version: 0.1
#Date: 9/8/11
#Desription: Fun with Dice
####################

import random


class Dice:
    def __init__(self, sides = 6):
        self.sides = sides

    def roll(self):
        r = random.randint(1,self.sides)
        return r

    def rolltest(self, numtest):
        testScore = dict([(x,0) for x in range(1, self.sides + 1)])

        for x in range(numtest):
            testValue = self.roll()
            testScore[testValue] += 1

        return testScore

