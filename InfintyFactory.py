from tkinter import *
from tkinter import messagebox
import random
class factory_tile(Canvas):
    def __init__(self, master, floor, x, y):
        Canvas.__init__(self, master, bg='grey', height = 25, width = 25)
class factory_grid():
    def __init__(self, sg, root):
        self.floorPlan = []
        self.graphics_grid = sg
        floorOne = []
        for x in range(10):
            for y in range(10):
                tile = factory_tile(self.graphics_grid, 0, x, y)
                tile.grid(row=y, column=x)
                floorOne.append(tile)
        """Buttons"""
        self.buttonFrame = Frame(root, bg='black')
        self.buttonFrame.grid(row=1, column = 0)
        self.buttonBuildMenu = Button(self.buttonFrame, command=self.openBuildMenu, height = 1, width = 15, text = 'Build Menu')
        self.buttonBuildMenu.grid(column=0, row=0)
        self.buttonResearchMenu = Button(self.buttonFrame, command=self.openResearchMenu, height = 1, width = 15, text = 'Research Menu')
        self.buttonResearchMenu.grid(column=1, row=0)
        self.buttonFloorUp = Button(self.buttonFrame, command=self.floorUp, height = 1, width = 15, text = 'Buy Next Floor')
        self.buttonFloorUp.grid(column=2, row=0)
        self.buttonFloorDown = Button(self.buttonFrame, command=self.floorDown, height = 1, width = 15, text = 'Down')
        self.buttonFloorDown.grid(column=3, row=0)
        """Menu"""
        self.menu = Frame(root, bg='black')
        self.menu.grid(row=1,column=1)
        self.tier = 0
    def tick(self):
    def openBuildMenu(self):
        return
    def openResearchMenu(self):
        global research
        if research >= 10^self.tier
            resourceOption = {'name':random.choice([]) + random.choice([]), 'bitmap':self.generateBitmap()]
    def floorUp(self):
        global floor, money
        if floor + 1 >= len(self.floorPlan):
            if money >= 1000 * (floor+1)^2
                money = money - 1000 * (floor+1)^2
                self.createNewFloor()
                floor + 1
        else:
            floor+1
    def createNewFloor(self):
        return
    def generateBitmap(self):
        return
    def floorDown(self):
        global floor
        if not floor - 1 < 0:
            floor = floor - 1 
class graphics_grid(Frame):
    def __init__(self, root):
        Frame.__init__(self, root, bg = 'black')
        self.grid(row=0, column=0)
def factor():
    """global setup"""
    global floor, money, energy, research
    floor = 0
    money = 500
    energy = 0
    research = 0
    """Tkinter&object setup"""
    root = Tk()
    frame = Frame(root)
    frame.grid()
    root.title('InfinteFactory')
    sg = graphics_grid(frame)
    main_grid = factory_grid(sg, frame)
    root.mainloop()
factor()
