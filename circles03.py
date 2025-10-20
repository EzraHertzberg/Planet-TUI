"""
Circle function made to work with a simple grid
also lets get some rotation
"""
import math
import os
import time

size = os.get_terminal_size()
screen_width = size.columns 
screen_height = size.lines - 4

grid = []

def grid_set():
    global grid
    for j in range(screen_height):
        row_arr = []
        for i in range(screen_width):
            row_arr.append("█")
        grid.append(row_arr)


def grid_call():
    global grid
    for i in range(screen_height):
        print("".join(grid[i]))


class circle:
        def __init__(self,x, y, size):
            self.x = x
            self.y = y
            self.size = size
        def draw(self):
            for i in range(self.size):
                if i < self.size // 2:
                    e = i + self.size//2
                else:
                    e = self.size + self.size//2 -1 - i
                
                for j in range(-e, e):
                    try:
                        if grid[self.y + i][self.x + j]:
                            grid[self.y + i][self.x + j] = " " 
                    except IndexError:
                        pass  
                    
if __name__ == "__main__":
    grid_set()
    circ1 = circle(80,20,10)
    circ2 = circle(60,20,5)
    circ3 = circle(60,20,3)
    rot = 0
    rot2 = 90
    while True:
        grid = []
        grid_set()
        rot += 0.1
        rot2 += 0.2
        circ2.x = 80 + round(math.sin(rot) * 30)
        circ2.y = 22 + round(math.cos(rot) * 15)
        circ3.x = circ2.x + round(math.sin(rot2) * 20)
        circ3.y = circ2.y + round(math.cos(rot2) * 10)
        circ1.draw()
        circ2.draw()
        circ3.draw()
        print("\033[H", end="")
        grid_call()
        time.sleep(0.05)
