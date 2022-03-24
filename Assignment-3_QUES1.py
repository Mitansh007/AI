#Assignment-3 Q1
import math

start = [[2,0,3],
         [1,8,4],
         [7,6,5]]
goal = [[1,2,3],
        [8,0,4],
        [7,6,5]]

sum1=0.0
#This functions return the position of that particular element in the goal state
def getsaloni(ele,s=goal):
    for i in range(3):
        for j in range(3):
            if(s[i][j]==ele):
                return i,j

#This function calculates the euclidian distance between the elements of the
#goal state and the final state using distance between 2 points formula

def euclidian(s):
    global sum1
    for x1 in range(3):
        for y1 in range(3):
            x2,y2 = getsaloni(s[x1][y1])
            sum1 += math.sqrt((x2-x1)**2 + (y2-y1)**2)
    print("The Euclidian distance is:",sum1)
    sum1=0.0

#This function calculates the manhattan or city block distance 
#between the elements of the goal state and the final state using 
#simple mathematical operations

def manhattan(s):
    global sum1
    for x1 in range(3):
        for y1 in range(3):
            x2,y2 = getsaloni(s[x1][y1])
            sum1 += abs(x2-x1) + abs(y2-y1)
    print("The Manhattan distance is:",sum1)
    sum1=0.0

#This function calculates the minkowiski distance 
#between the elements of the goal state and the final state.
#This distance is a combination of both the distances mentioned above taking the generalisation as 
# p=1 for manhattan and p=2 for euclidian

def minkowiski(s):
    global sum1
    p=3
    for x1 in range(3):
        for y1 in range(3):
            x2,y2 = getsaloni(s[x1][y1])
            sum1 += ((abs(x2-x1)**p) + (abs(y2-y1))**p)**(1./p)
    print("The Minkowiski distance is:",sum1)
    sum1=0.0

euclidian(start)
manhattan(start)
minkowiski(start)