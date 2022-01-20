import math

grid1=[]
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

grid = [
"+++++++++++++++++++++++++++++++++++++++++++++++++++",
"+               +                                 +",
"+  ++++++++++  +++++++++++++  +++++++  ++++++++++++",
"+s          +                 +               ++  +",
"+  +++++++  +++++++++++++  +++++++++++++++++++++  +",
"+  +     +  +           +  +                 +++  +",
"+  +  +  +  +  +  ++++  +  +  +++++++++++++  +++  +",
"+  +  +  +  +  +  +        +  +  +        +       +",
"+  +  ++++  +  ++++++++++  +  +  ++++  +  +  ++   +",
"+  +     +  +          +   +           +  +  ++  ++",
"+  ++++  +  +++++++ ++++++++  +++++++++++++  ++  ++",
"+     +  +     +              +              ++   +",
"++++  +  ++++++++++ +++++++++++  ++++++++++  +++  +",
"+  +  +                    +     +     +  +  +++  +",
"+  +  ++++  +++++++++++++  +  ++++  +  +  +  ++   +",
"+  +  +     +     +     +  +  +     +     +  ++  ++",
"+  +  +  +++++++  ++++  +  +  +  ++++++++++  ++  ++",
"+                       +  +  +              ++  ++",
"+ ++++++             +  +  +  +  +++        +++  ++",
"+ ++++++ ++++++ +++++++++    ++ ++   ++++++++++  ++",
"+ +    +    +++ +     +++++++++ ++  +++++++    + ++",
"+ ++++ ++++ +++ + +++ +++    ++    ++    ++ ++ + ++",
"+ ++++    +     + +++ +++ ++ ++++++++ ++ ++ ++   ++",
"+      ++ +++++++e+++     ++          ++    +++++++",
"+++++++++++++++++++++++++++++++++++++++++++++++++++",
 ]

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

openlist=[]
closelist=[]
start = gridob[x1][y1]
end = gridob[x2][y2]
openlist.append(start)

def Astar():
    while len(openlist) > 0:
        # print("Items in openlist")
        # for i in range(len(openlist)):
        #    print(openlist)
        #print("Items in closedlist")
        #for i in range(len(closelist)):
        #   print(closelist)
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
                if path[k].i==x1 and path[k].j:
                    grid1[path[k].i][path[k].j]=3
                else:
                    grid1[path[k].i][path[k].j]=1
            for k in range(count1):
                print("\n")
                for l in range(count2):
                    print(grid1[k][l],end="")
        openlist.remove(current)
        closelist.append(current)
        neighbourslist=current.neighbours
        #print(neighbourslist)
        for i in range(len(neighbourslist)):
            neighbour=neighbourslist[i]
            if neighbour not in closelist and not neighbour.wall:
                tempg = current.g+1
                if neighbour in openlist:
                    if tempg < neighbour.g:
                        neighbour.g = tempg
                else:
                    neighbour.g = tempg
                    openlist.append(neighbour)
                neighbour.h=math.sqrt((math.pow(end.i-neighbour.i,2))+(math.pow(end.j-neighbour.j,2)))
                neighbour.f=neighbour.g+neighbour.h
                neighbour.previous=current

Astar()
