"""
Live accurate solar system
"""
import math
import os
import time
import random
import angle_calc
from skyfield.api import load
ts = load.timescale()
the_time = ts.now()

size = os.get_terminal_size()
screen_width = size.columns 
screen_height = size.lines - 2

commands = ["h","timeset","solarsystem"]

grid = []

def set_new_time():
    while True:
        year = input("Enter a date mm/dd/yyyy between or n for the current time: ")
        if year == "n":
            the_time = ts.now()
            break
        
        
def grid_set():
    global grid
    for j in range(screen_height):
        row_arr = []
        for i in range(screen_width):
            row_arr.append(" ")
        grid.append(row_arr)


def grid_call():
    global grid
    for i in range(screen_height):
        print("".join(grid[i]))


class circle:
        def __init__(self,x, y, size, name):
            self.x = x
            self.y = y
            self.size = int(size)
            self.name = name
            
        def draw(self):
            for i in range(self.size):
                if i < self.size // 2:
                    e = i + self.size//2
                else:
                    e = self.size + self.size//2 -1 - i
                
                for j in range(-e, e):
                    try:
                        if grid[(self.y - self.size//2) + i][self.x + j]:
                            grid[(self.y - self.size//2) + i][self.x + j] = "█" 
                    except IndexError:
                        pass  
            for k in range(len(self.name)):
                try:
                     if grid[(self.y - self.size//2) + self.size][self.x + k]:
                        grid[(self.y - self.size//2) + self.size][self.x + k] = self.name[k] 
                except IndexError:
                    pass          
        def orbit(self, origin, dist, init_ang, speed):  
            if not hasattr(self, "ang"):
                self.ang = init_ang * math.pi / 180
            self.x = round(origin.x + math.cos(self.ang) * 2 * dist)
            self.y = round(origin.y - math.sin(self.ang) * dist)
            self.ang = self.ang + speed

def solar_system():
    os.system("cls")
    grid_set()
    sun = circle(80,25,4,"sun")
    planets = ["place holder",
               circle(60,20,3, "mercury"),
               circle(60,20,3,"venus"),
               circle(60,20,3., "earth"),
               circle(60,20,3, "mars"),
               circle(60,20,3, "jupiter"),
               circle(60,20,3, "saturn"),
               circle(60,20,3, "uranus"),
               circle(60,20,3, "neptune"),
               ]
    grid_set()
    sun.draw()
    for i, planet in enumerate(planets):
        if i > 0:
            planet.orbit(sun, 6 + i * 3, angle_calc.calc_angle(i, the_time), 0) 
            planet.draw()
            grid_call()
        
        
if __name__ == "__main__":
    while True:
        inp = input("Enter a command, h for help: ")
        if inp in commands:
            if inp == "solarsystem":
                solar_system()
            if inp == "h":
                print("These are the valid commands: ")
                for com in commands:
                    print(com)
            if inp == "time_set":
                set_new_time()
        else:
            print("that's not a command")