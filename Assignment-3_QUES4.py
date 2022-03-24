import copy
from queue import PriorityQueue as pq
from math import sqrt
# Manhattan
openState=[]
closedState=[]
bfsState=pq()
initialState=[[2, 0, 3], [1, 8, 4], [7, 6, 5]]
goalState=[[1, 2, 3], [8, 0, 4], [7, 6, 5]]

# finding blank tile
def findBlankTile(currentState):
    for i in range(3):
        for j in range(3):
            if currentState[i][j]==0:
                r,c=i,j
                return r,c

#moving blank tile upwards
def moveUp(currentState, r, c):
    if r != 0:
        child = copy.deepcopy(currentState)
        child[r][c],child[r - 1][c] = (child[r - 1][c],0)
        if child not in openState and child not in closedState:
            countTest=manhattanDistance(goalState,child)
            bfsState.put((countTest, child))
            openState.append(child)
            return child
    return None

#moving blank tile downwards
def moveDown(currentState, r, c):
    if r != 2:
        child = copy.deepcopy(currentState)
        child[r][c], child[r+1][c] = (child[r+1][c],0)
        if child not in openState and child not in closedState:
            countTest=manhattanDistance(goalState,child)
            bfsState.put((countTest, child))
            openState.append(child)
            return child
    return None

#moving blank tile leftwards
def moveLeft(currentState, r, c):
    if c != 0:
        child = copy.deepcopy(currentState)
        child[r][c], child[r][c-1] = (child[r][c-1],0)
        if child not in openState and child not in closedState:
            countTest=manhattanDistance(goalState,child)
            bfsState.put((countTest, child))
            openState.append(child)
            return child
    return None

#moving blank tile rightwards
def moveRight(currentState, r, c):
    if c != 2:
        child = copy.deepcopy(currentState)
        child[r][c], child[r][c+1] = (child[r][c+1],0)
        if child not in openState and child not in closedState:
            countTest=manhattanDistance(goalState,child)
            bfsState.put((countTest, child))
            openState.append(child)
            return child
    return None


def isGoal(currentState,goalState):
    if currentState==goalState:
        return True
    return False

def manhattanDistance(goalState, currentState):
    blockValue=0
    totalDist=0
    while blockValue<9:
        for i in range(3):
            for j in range(3):
                if goalState[i][j]==blockValue:
                    rg,cg=i,j
                if currentState[i][j]==blockValue:
                    rc,cc=i,j
        blockValue+=1
        totalDist=abs(rg-rc)+abs(cg-cc)
    
    return totalDist
        

def search():
    countTest=manhattanDistance(goalState,initialState)
    bfsState.put((countTest, initialState))
    x=bfsState.get()
    flag=1
    while flag:
        currentState=x[1]
        if isGoal(currentState,goalState):
            flag = 0
#             print(len(closedState))
        else:
            r,c=findBlankTile(currentState)
            neighbour=[0]*4
            neighbour[0]=moveUp(currentState,r,c)
            neighbour[1]=moveDown(currentState,r,c)
            neighbour[2]=moveLeft(currentState,r,c)
            neighbour[3]=moveRight(currentState,r,c)
            x=bfsState.get()
            closedState.append(x[1])
            if x[1]==goalState:
                print(closedState)
                print(len(closedState))
    
    
    
search()