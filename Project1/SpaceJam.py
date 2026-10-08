
from direct.showbase.ShowBase import ShowBase

#new imports for lab 2
import DefensePaths as defensePaths
import SpaceJamClasses as spaceJamClasses


class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.Universe = spaceJamClasses.Universe(self.loader, "./Assets/Universe/Universe.x", self.render, 'Universe', "./Assets/Universe/Universe.jpg", (0, 0, 0), 10000)
        self.Planet1 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Planet1', "./Assets/Planets/Planet1.jpg", (-6000, -3000, -800), 250)
        self.Planet2 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Planet2', "./Assets/Planets/Planet2.jpg", (0, 6000, 0), 300)
        self.Planet3 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Planet3', "./Assets/Planets/Planet3.jpg", (500, -5000, 200), 500)
        self.Planet4 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Planet4', "./Assets/Planets/Planet4.jpg", (300, 6000, 500), 150)
        self.Planet5 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Planet5', "./Assets/Planets/Planet5.jpg", (700, -2000, 100), 500)
        self.Planet6 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Planet6', "./Assets/Planets/Planet6.jpg", (0, -900, -1400), 700)
        self.SpaceStation1 = spaceJamClasses.SpaceStation(self.loader, "./Assets/Space Station/spaceStation.egg", self.render, 'Space Station', "./Assets/Space Station/SpaceStation1_Dif2.png", (1500, 1000, -100), 40)
        self.Hero = spaceJamClasses.Spaceship(self.loader, "./Assets/Spaceships/Dumbledore.egg", self.render, 'Hero', "./Assets/Spaceships/spacejet_C.png", Vec3(1000, 1200, -50), 50)
        




#all new functions for lab 2

    #def DrawBaseballSeams(self, centralObject, droneName, step, numSeams, radius = 1):
        #unitVec = defensePaths.BaseballSeams

app = MyApp()
app.run()