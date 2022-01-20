import turtle                    
import time
from collections import deque
import math

print("\n\t\tMENU\n")
print("1:To use BFS for path searching\n")
print("2:To use  A* for path searching\n")
n=int(input("Enter your choice and chech your task bar: "))
      
scc=turtle.Turtle()             # import all functions of turtle to scc
wn = turtle.Screen()            # define t screen
wn.bgcolor("black")             # to set the background colour of output screen
wn.title("Automatic Mesh Solver")
wn.setup(1400,800)              #dimension of output sceen

Sx=0
Sy=0
Ex=0
Ey=0

map = [
   "________________________________________________________e___",
   "_____  ___   ___________  ____ _                           _",
   "_____  ___   ___________            _____ _______   ___ __ _",
   "_____                     ____ __________ _______ _ ___ __ _",
   "__    ________ _ ________      __         _______ _   _ __ _",
   "__ __ ________ _ ___________ __ _ ___ __  ___   _ ___ _ __ _",
   "__  _      ___     ___    __    _ _ _ __    _ _   ___ _    _",
   "__  _  ___ _____ _ ___ __ __    _ _ _ __    _ _   ___ _    _",
   "__  ______ _____ _ ___ __ _______ _ _    ____ ____  _   __ _",
   "__  ______ __    _ ___ _  __    _   ___    __ ____  ___    _",
   "__       _ _  _    ___ _  __ __ _ _ ______ __ ____  ___    _",
   "__  ____ _ _ __        _  __ __   _      _    ____    ___  _",
   "__  ____ _ _   _________     __   _________        __ ___  _",
   "__  ____ _____ _____________ __ _ ___ __    _   _ ___ ___  _",
   "__         ___     ___    __    _ _ _ __    _ _   ___ _    _",
   "___ _  ___ _____ _ ___ __ __    _ _ _ __    _ _   ___ _    _",
   "_   ______ _____ _ ___ __ _______ _ _   __ __ ____  _    _ _",
   "__________ __    _ ___ _  __    _   ___    __ ____  ___  _ _",
   "_        _ _  _    ___ _  __ __ _ _ ______ __ ____  ___    _",
   "_   ____ _ _ __        _  __ __   _      _    ____    ____ _",
   "___ ____ _ _   _________     ___ __________        __ ___  _",
   "___ ____   ___ ______    _______         __  ___ ____      _",
   "___    _       __     _________________     _    ________  _",
   "___ __   ____         _________________ __  _____________  _",
   "_   ____ _ _ __       __  __ __   _      _    ____    ___  _",
   "___ ____ _ _   __ __  __         __________           ___  _",
   "___ ____   ___ __ __         __              ___           _",
   "___    _       __ ______________                 ___________",
   "___ __            ______________                 ___________",
   "___s________________________________________________________"

 ]


# class for the obstacles/wall
class Obstacle(turtle.Turtle):               
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")           # the turtle shape
        self.color("brown")             # colour of the turtle
        self.penup()                    # lift up the pen so it do not leave a trail
        self.speed(0)                   # time delay between two tutrtle objects


# this is the class for the start
class RedColour(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.penup()
        self.speed(0)

# this is the class for the goal state
class GreenColour(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)

class Black(turtle.Turtle):         #"JUGAAD" for getting full black screen
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black")

#==========================================================================================================================================
if n==1:
    turtle.color('red')
    turtle.penup()
    turtle.goto(-220,350)
    style = ('Courier', 20, 'italic')
    turtle.write('Welcome to the Automatic Mesh Solver with ', font=style, align='center')
    turtle.goto(340,350)
    style = ('Courier', 20, 'bold')
    turtle.write('Bredth First Search Technique', font=style, align='center')
    turtle.hideturtle()
    time.sleep(3)
    def createMap(map):                    # define a function called setup_maze
        global Sx, Sy, Ex, Ey      # set up global variables for start and end locations
        for y in range(len(map)):                 # read in the map line by line means 10 times
            for x in range(len(map[y])):          # read each cell in the line means 16 times
                char = map[y][x]             # assign the varaible "character" the the x and y location of the map
                bound_x = -600 + x * 20            # x axis for global boundary
                bound_y = 288 - y * 20            # y axis shift global boundary
                if char == "_":
                    route.goto(bound_x, bound_y)        # move pen to the x and y locaion and
                    route.stamp()                       # stamp a copy of the turtle on the screen
                    walls.append((bound_x, bound_y))    # add coordinate to walls list

                if char == " " or char == "e":
                    path.append((bound_x, bound_y))     # add " " and e to path list

                if char == "e":
                    green.color("green")
                    green.goto(bound_x, bound_y)       # send green sprite to screen location
                    Ex, Ey = bound_x,bound_y     # assign end locations variables to end_x and end_y
                

                if char == "s":
                    red.color("red")
                    Sx, Sy = bound_x, bound_y  # assign start locations variables to start_x and start_y
                    red.goto(bound_x, bound_y)
                if char == "X":
                    red.color("red")
                    Sx, Sy = bound_x, bound_y  # assign start locations variables to start_x and start_y
                    red.goto(bound_x, bound_y)
            #print("[",bound_x,bound_y,"]",end=" ")
       # print('\n')

#===========================================================================================================================================
# def search(x,y) function for searching goal state form start point

    def search(x,y):
        Dict[x,y] = x,y
        q.append((x, y))
        while len(q) > 0:          # exit while loop when length queue equals zero
        #time.sleep(1)
            x, y = q.popleft()     # pop next entry in the frontier queue an assign to x and y location

            if(x - 20, y) in path and (x - 20, y) not in visited:  # check the cell on the left
                Dict[x - 20, y] = x, y    # backtracking routine [cell] is the previous cell. x, y is the current cell
                q.append((x - 20, y))   # add coordinate to frontier list
                visited.add((x-20, y))  # add coordinate to visited list
            #print("[",x - 20, y,"]",end=" ")
            if (x, y - 20) in path and (x, y - 20) not in visited:  # check the cell down
                Dict[x, y - 20] = x, y
                q.append((x, y - 20))
                visited.add((x, y - 20))
            #print("[",x - 20, y,"]",end=" ")
            if(x + 20, y) in path and (x + 20, y) not in visited:   # check the cell on the  right
                Dict[x + 20, y] = x, y
                q.append((x + 20, y))
                visited.add((x + 20, y))
           # print("[",x - 20, y,"]",end=" ")
            if(x, y + 20) in path and (x, y + 20) not in visited:  # check the cell up
                Dict[x, y + 20] = x, y
                q.append((x, y + 20))
                visited.add((x, y + 20))
           # print("[",x - 20, y,"]",end=" ")
       # print('\n')  
            red.goto(x,y)
            red.stamp()
            x, y = Dict[x, y]               # "key value" now becomes the new key

#==========================================================================================================================================
# def backtrack(x, y) function for backtracking from goal state to start state

    def backtrack(x, y):
        green.goto(x, y)
        green.stamp()
        while (x, y) != (Sx, Sy):    # stop loop when current cells == start cell
            #time.sleep(1)
            green.goto(Dict[x, y])        # move the green colour to the key value of solution ()
            green.stamp()
            x, y  = Dict[x, y]               # "key value" now becomes the new key
       # print(x,y,"||")


    """map = [
     "__e_",
     "_  _",
     "_s _"
     ]

    """
 

#=======================================main body starts here         
    route = Obstacle()
    red = RedColour()
    green = GreenColour()
    black= Black()
#======================#
    walls = []                              #List to have coordinates of + symbol
    path = []                               # list to have coordinates of " " and "e" symbol
    visited = set()                         #keep track on left square right square above coordinates and below coordinates of curret coordinate.
    q = deque()                             #To creat solution
    Dict = {}                           # solution dictionary of coordinates for backtracking
#======================#
    createMap(map)
    time.sleep(1)
    search(Sx,Sy)                           #Search starting coordinate
    backtrack(Ex, Ey)                       #backtrack coordinate

#=========================================================================================================================================
#======================================================== A STAR==========================================================================
#=========================================================================================================================================

if n==2:
    turtle.color('red')
    turtle.penup()
    turtle.goto(-220,350)
    style = ('Courier', 20, 'italic')
    turtle.write('Welcome to the Automatic Mesh Solver with ', font=style, align='center')
    turtle.goto(340,350)
    style = ('Courier', 20, 'bold')
    turtle.write('A* (A Star) Search Technique', font=style, align='center')
    turtle.hideturtle()
    time.sleep(3)

    grid=[]
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
                Sx,Sy=i,j
            if grid[i][j]=="e": 
                grid1[i].append(3)
                Ex,Ey=i,j
            if grid[i][j]==" ":
                grid1[i].append(0)



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
    start = gridob[Sx][Sy]
    end = gridob[Ex][Ey]
    openlist.append(start)

    def setup_maze(grid):                          # define a function called setup_maze
        global start_x, start_y, end_x, end_y      # set up global variables for start and end locations
        for y in range(len(grid)):                 # read in the grid line by line
            for x in range(len(grid[y])):          # read each cell in the line
                character = grid[y][x]             # assign the varaible "character" the the x and y location od the grid
                screen_x = -588 + (x * 21)         # move to the x location on the screen staring at -588
                screen_y = 288 - (y * 21)          # move to the y location of the screen starting at 288

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
                    red.stamp()
    
        
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
                
                    if path[k].i==Sx and path[k].j==Sy:
                        grid1[path[k].i][path[k].j]=3
                    else:
                        grid1[path[k].i][path[k].j]=1
           
                return
                
            openlist.remove(current)
            closelist.append(current)
            neighbourslist=current.neighbours
            for i in range(len(neighbourslist)):
                neighbour=neighbourslist[i]
                if neighbour not in closelist and not neighbour.wall:
                    time.sleep(0)
                    red.goto(-588 + (neighbour.j * 21), 288 - (neighbour.i * 21))
                    red.stamp()
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
       
   
            grid2.append([])
      
    
    
        for i in range(len(grid1)):
            for j in range(len(grid1[i])):
                screen_x = -588 + (j * 21)
                screen_y = 288 - (i * 21)          
  
                if grid1[i][j] == 2:
                    maze.goto(screen_x, screen_y)         
                    maze.stamp()                          
                
                if grid1[i][j] == 3:
                    green.goto(screen_x, screen_y)       
                    green.stamp()
                

                if grid1[i][j] == 1:
                    green.goto(screen_x, screen_y)
                    green.stamp()
    maze = Obstacle()
    red = RedColour()
    green = GreenColour()
    black=Black()
    
    setup_maze(grid)
    Astar()
    backtrack(grid,grid1)
    wn.exitonclick()

else:
    print("\nWRONG INPUT GIVEN")

