# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 13:33:23 2022

@author: Jeremy
"""
from random import *

class MyClass(object):  


    def greet(self):
        print("Hello World")


class MyNextClass(object):

    def greetAgain(self):
        print("Hello again")
        
class Entity(object):
    
    type = ""
    xLoc = 0
    yLoc = 0
    
    def __init__(self, type, xLoc, yLoc):
        self.type = type
        self.xLoc = xLoc
        self.yLoc = yLoc
        
    def __str__(self):
        return "Type: " + str(self.type) + ", X: " + str(self.xLoc) + ", Y: " + str(self.yLoc)
        
class World(object):
    
    xLength = 0
    yLength = 0  
    nEnemies = 0
    entities = []
    character = None
    enemies = []
    
    
    def __init__(self, xlen, ylen):
        self.xLength = xlen
        self.yLength = ylen
        self.nEnemies = 2
        self.character = Entity("Character", randint(0, xlen-1), randint(0, ylen-1))
        
    
    def generateMap(self):
        print ("X len:", self.xLength)

        # Create Stones
        for x in range(self.xLength):
            for y in range(self.yLength):
                if random() < .1:
                    self.entities.append(Entity("Stone", x, y))
                    
        #Create Character
        # self.entities.append()
        
        #Create Enemies
        for n in range(self.nEnemies):
            self.enemies.append(Entity("Enemy", randint(0, self.xLength-1), randint(0, self.yLength-1)))
            
        
    def printEntities(self):
        for entity in self.entities:
            print(entity)
        print(self.character)
        for entity in self.enemies:
            print(entity)
        
if __name__ == "__main__":
    myWorld = World(100, 100)
    myWorld.generateMap()
    myWorld.printEntities()