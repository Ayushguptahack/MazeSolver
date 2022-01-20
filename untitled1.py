import math
import turtle                    # import turtle library
import time
import sys


grid1=[]
grid2=[]
gridob=[]
width=0
height=0
count1=0
count2=0
count3=0
path = None
start = None
end = None
x1 = 0
x2 = 0
y1 = 0
y2 = 0
#a=input("Enter Number of rows:  ")
#b=input("Enter Number of columns: ")
wn = turtle.Screen()               # define the turtle screen
wn.bgcolor("black")                # set the background colour
wn.title("An A* Maze Solving Program")
wn.setup(1300,700)

#grid = [
# "+++++++++++++++",
# "+s+       + +e+",
# "+ +++++ +++ + +",
# "+ + +       + +",
# "+ +   +++ + + +",
# "+ + + +   + + +",
# "+   + +   + + +",
# "+++++ +   + + +",
# "+     +   +   +",
# "+++++++++++++++",
# ]

#grid = [
# "+++++++++",
# "+ ++s++++",
# "+ ++ ++++",
# "+ ++ ++++",
# "+    ++++",
# "++++ ++++",
# "++++ ++++",
# "+      e+",
# "+++++++++",
# ]

#grid = [
# "+++++++++++++++",
# "+             +",
# "+             +",
# "+             +",
# "+     e       +",
# "+             +",
# "+             +",
# "+             +",
# "+ s           +",
# "+++++++++++++++",
# ]

#grid = [
#"+++++++++++++++++++++++++++++++++++++++++++++++++++",
#"+               +                                 +",
#"+  ++++++++++  +++++++++++++  +++++++  ++++++++++++",
#"+s          +                 +               ++  +",
#"+  + +++++  +++++++++++++  +++++++++++++++++++++  +",
#"+  +     +  +           +  +                 +++  +",
#"+  +  +  +  +  +  ++++  +  +  +++++++++++++  +++  +",
#"+  +  +  +  +  +  +        +  +  +        +       +",
#"+  +  ++++  +  ++++++++++  +  +  ++++  +  +  ++   +",
#"+  +     +  +          +   +           +  +  ++  ++",
#"+  ++++  +  +++++++ ++++++++  +++++++++++++  ++  ++",
#"+     +  +     +              +              ++   +",
#"++++  +  ++++++++++ +++++++++++  ++++++++++  +++  +",
#"+  +  +                    +     +     +  +  +++  +",
#"+  +  ++++  +++++++++++++  +  ++++  +  +  +  ++   +",
#"+  +  +     +     +     +  +  +     +     +  ++  ++",
#"+  +  +  +++++++  ++++  +  +  +  ++++++++++  ++  ++",
#"+                       +  +  +              ++  ++",
#"+ ++++++             +  +  +  +  +++        +++  ++",
#"+ ++++++ ++++++ + +++++++    ++ ++   ++++++++++  ++",
#"+ +    +    +++ +     +++++++++ ++  +++++++    + ++",
#"+ ++++ ++++ +++ + +++ +++    ++    ++    ++ ++ + ++",
#"+ ++++    +     + +++ +++ ++ ++++++++ ++ ++ ++   ++",
#"+      ++ +++++++e+++     ++          ++    +++++++",
#"+++++++++++++++++++++++++++++++++++++++++++++++++++",
#]
map = [
   "___________________e________________________________",
   "__  __   ____  ___ _                           _____",
   "__  __   ____            __ ___   _ __ _____________",
   "__                     __ ____ ___ _ __ __ _________",
   "_    ___ _ ___      _         ___ _   _ __ _________",
   "_ _ ___ _ ____ _ _ __ _  __   _ _ _ __ _____________",
   "_  _      __     _    _    _ _ _ _    _ _   _ _    _",
   "_  _  __ __ _ __ _ _    _ _ _ _    _ _   __ _    ___",
   "_  ___ __ _ __ _ ___ _ _    __ __  _   _ ___________",
   "_  ___ _    _ __ _  _    _   __    _ __  __    _____",
   "_       _ _  _    __ _  _ _ _ _ __ _ __  __    _____",
   "_  __ _ _ _        _  _ _   _      _    __    _  ___",
   "_  __ _ _   ____     _   ____        _ __  _________",
   "_  __ __ _____ _ _ __ _    _   _ __ _  _____________",
   "_         __     _    _    _ _ _ _    _ _   _ _    _",
   "_ _  _ __ _ __ _ _    _ _ _ _    _ _   __ _    _____",
   "_   __ __ _ __ _ ___ _ _   _ _ ___  _    _ _________",
   "____ _    _ __ _  _    _   __    _ __  __  _ _______",
   "_        _ _  _    _ _  _ _ _ _ __ _ __  __    _____",
   "_   __ _ _ _        _  _ _   _      _    __    ___ _",
   "_ __ _ _   ___     _ ____        _ __  _____________",
   "_ __   _ __    ___         _  __ __      ___________",
   "_    _       _     ______     _    ____  ___________",
   "_ _   __         ______ _  ______  _________________",
   "_   __ _ _ _       _  _ _   _      _    __    _  ___",
   "_ __ _ _   _ _  _         ____           __  _______",
   "_ __   _ _ _         _              __           ___",
   "_    _       _ _____                 _______________",
   "_ _            _____                 _______________",
   "__s_________________________________________________"

 ]
grid=[]
for i in range(len(map)):
    grid.append([])
    for j in range(len(map[i])):
        if(map[i][j]=="_"):
            grid[i].append("+")
        if(map[i][j]=="s"):
            grid[i].append("s")
        if(map[i][j]=="e"):
            grid[i].append("e")
        if(map[i][j]==" "):
            grid[i].append(" ")

print(grid)

for i in range(len(grid)):
    print("\n")
    for j in range(len(grid[i])):
        print(grid[i][j],end=" ")


class Maze(turtle.Turtle):               # define a Maze class
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")            # the turtle shape
        self.color("white")             # colour of the turtle
        self.penup()                    # lift up the pen so it do not leave a trail
        self.speed(0)
        
# this is the class for the finish line - green square in the maze
class Green(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)
        

class Blue(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)
        


# this is the class for the yellow or turtle
class Red(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.penup()
        self.speed(0)
        

class Yellow(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("yellow")
        self.penup()
        self.speed(0)
        

class spot():
    def __init__(self,i,j):
        self.i=i
        self.j=j
        self.g=0
        self.h=0
        self.f=0
        self.neighbours=[]
        self.previous= None
        self.wall=False
    
    def addneighbours(self,gridob):
        if i < count1-1:
            self.neighbours.append(gridob[i+1][j])
        if i > 0:
            self.neighbours.append(gridob[i-1][j])
        if j < count2-1:
            self.neighbours.append(gridob[i][j+1])
        if j > 0:
            self.neighbours.append(gridob[i][j-1])
        if i>0 and j>0:
            self.neighbours.append(gridob[i-1][j-1])
        if i>0 and j<count2-1:
            self.neighbours.append(gridob[i-1][j+1])
        if i<count1-1 and j>0:
            self.neighbours.append(gridob[i+1][j-1])
        if i<count1-1 and j<count2-1:
            self.neighbours.append(gridob[i+1][j+1])

for i in range(len(grid)):
    gridob.append([])
    count1 = len(grid)
    count2 = 0
    for j in range(len(grid[i])):
       gridob[i].append(0)
       count2=len(grid[i])

for i in range(len(grid)):
    grid1.append([])
    for j in range (len(grid[i])):
        if grid[i][j]=="+":
            grid1[i].append(2)
        if grid[i][j]=="s": 
            grid1[i].append(3)
            x1,y1=i,j
        if grid[i][j]=="e": 
            grid1[i].append(3)
            x2,y2=i,j
        if grid[i][j]==" ":
            grid1[i].append(0)

    
for k in range(count1):
    print("\n")
    for l in range(count2):
        print(grid1[k][l],end="")

for i in range(len(grid)):
    for j in range(len(grid[i])):
        gridob[i][j]=spot(i,j)
        

for i in range(len(grid)):
    for j in range(len(grid[i])):
        gridob[i][j].addneighbours(gridob)
        if grid[i][j]=="+":
            gridob[i][j].wall = True

openlist=[]
closelist=[]
start = gridob[x1][y1]
end = gridob[x2][y2]
openlist.append(start)

def setup_maze(grid):                          # define a function called setup_maze
    global start_x, start_y, end_x, end_y      # set up global variables for start and end locations
    for y in range(len(grid)):                 # read in the grid line by line
        for x in range(len(grid[y])):          # read each cell in the line
            character = grid[y][x]             # assign the varaible "character" the the x and y location od the grid
            screen_x = -588 + (x * 22)         # move to the x location on the screen staring at -588
            screen_y = 288 - (y * 22)          # move to the y location of the screen starting at 288

            if character == "+":
                maze.goto(screen_x, screen_y)         # move pen to the x and y locaion and
                maze.stamp()                          # stamp a copy of the turtle on the screen
                
            if character == "e":
                green.color("purple")
                green.goto(screen_x, screen_y)       # send green sprite to screen location
                end_x, end_y = screen_x,screen_y     # assign end locations variables to end_x and end_y
                green.stamp()
                green.color("green")

            if character == "s":
                start_x, start_y = screen_x, screen_y  # assign start locations variables to start_x and start_y
                red.goto(screen_x, screen_y)

    
def endProgram():
    wn.exitonclick()
    sys.exit()
    
def Astar():
    while len(openlist) > 0:
        
        lowestindex = 0
        for i in range(len(openlist)):
            if openlist[i].f<openlist[lowestindex].f:
                lowestindex = i

        current = openlist[lowestindex]
        if current == end:
            path = []
            temp=current
            while temp.previous:
                path.append(temp.previous)
                temp =temp.previous
            for k in range(len(path)):
                print("index i j",path[k].i,path[k].j,"\n")
                if path[k].i==x1 and path[k].j==y1:
                    grid1[path[k].i][path[k].j]=3
                else:
                    grid1[path[k].i][path[k].j]=1
            for k in range(count1):
                print("\n")
                for l in range(count2):
                    print(grid1[k][l],end="")
            return
                
        openlist.remove(current)
        closelist.append(current)
        neighbourslist=current.neighbours
        for i in range(len(neighbourslist)):
            neighbour=neighbourslist[i]
            if neighbour not in closelist and not neighbour.wall:
                time.sleep(0)
                green.goto(-588 + (neighbour.j * 22), 288 - (neighbour.i * 22))
                green.stamp()
                tempg = current.g+1
                newpath=False
                if neighbour in openlist:
                    if tempg < neighbour.g:
                        neighbour.g = tempg
                        newpath = True
                else:
                    neighbour.g = tempg
                    newpath = True
                    openlist.append(neighbour)
                if newpath:
                    neighbour.h=math.sqrt((math.pow(end.i-neighbour.i,2))+(math.pow(end.j-neighbour.j,2)))
                    neighbour.f=neighbour.g+neighbour.h
                neighbour.previous=current
            if neighbour in closelist and not neighbour.wall:
                blue.goto(-588 + (neighbour.j * 22), 288 - (neighbour.i * 22))
                blue.stamp()
                
def backtrack(grid,grid1):
    for i in range(len(grid)):
        grid2.append([])
        for j in range (len(grid[i])):
            if grid[i][j]=="+":
                grid2[i].append("+")
            if grid[i][j]=="s": 
                grid2[i].append("s")
            if grid[i][j]=="e": 
                grid2[i].append("e")
            if grid[i][j]==" " and grid1[i][j]==1:
                grid2[i].append("*")
            if grid[i][j]==" " and grid1[i][j]==0:
                grid2[i].append(" ")           
   
    for i in range(len(grid)):
        grid2.append([])
        print("\n")
        for j in range(len(grid[i])):
            print(grid2[i][j],end="")
    
    
    for i in range(len(grid1)):
        for j in range(len(grid1[i])):
            screen_x = -588 + (j * 22)
            screen_y = 288 - (i * 22)          

            if grid1[i][j] == 2:
                maze.goto(screen_x, screen_y)         
                maze.stamp()                          
                
            if grid1[i][j] == 3:
                red.goto(screen_x, screen_y)       
                red.stamp()
                

            if grid1[i][j] == 1:
                yellow.goto(screen_x, screen_y)
                yellow.stamp()
maze = Maze()
red = Red()
blue = Blue()
green = Green()
yellow = Yellow()

setup_maze(grid)
Astar()
backtrack(grid,grid1)
wn.exitonclick()
