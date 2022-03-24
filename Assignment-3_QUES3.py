#Assignment-3 Q3

import copy

start=[[2,0,3],
     [1,8,4],
     [7,6,5]]
goalSaloni=[[1,2,3],
       [8,0,4],
       [7,6,5]]
queue=[]

#This functions gives back the position of empty block represented by zero 
#after traversing the entire matrix

def getpos(s):
    for i in range(3):
        for j in range(3):
            if(s[i][j]==0):
                return i,j

#This functions check whether the state we have and the goal state matches

def compare(s,t):
    if s==t:
        return 1
    return 0

#The ups function does the up operation for us on the matrix if possible 
#by swapping the value of zero and the element above it

def ups(s,pos):
    i=pos[0]
    j=pos[1]
    if i==0:
        return s
    else:
        temp=copy.deepcopy(s)
        temp[i][j],temp[i-1][j]=temp[i-1][j],temp[i][j]
        return temp

#The downs function does the down operation for us on the matrix if possible 
#by swapping the value of zero and the element below it

def downs(s,pos):
    i=pos[0]
    j=pos[1]
    if i==2:
        return s
    else:
        temp=copy.deepcopy(s)
        temp[i][j],temp[i+1][j]=temp[i+1][j],temp[i][j]
        return temp

#The lefts function does the left operation for us on the matrix if possible 
#by swapping the value of zero and the element beside it

def lefts(s,pos):
    i=pos[0]
    j=pos[1]
    if j==0:
        return s
    else:
        temp=copy.deepcopy(s)
        temp[i][j-1],temp[i][j]=temp[i][j],temp[i][j-1]
        return temp

#The rights function does the right operation for us on the matrix if possible 
#by swapping the value of zero and the element beside it

def rights(s,pos):
    i=pos[0]
    j=pos[1]
    if j==2:
        return s
    else:
        temp=copy.deepcopy(s)
        temp[i][j+1],temp[i][j]=temp[i][j],temp[i][j+1]
        return temp

#This is the heurestic function which compares the current state and the final 
#state returning the total count of misplaced tiles in the state

def misplaced(s,final=goalSaloni):
    count=0
    for i in range(3):
        for j in range(3):
           if(s[i][j]!=final[i][j]):
               count+=1
    return count

#It is the main function which returns the best child of the incoming parent
#which has not been visited already after comparing it with other 
#children.

def getminnewstates(start):
    state=[]
    i,j=getpos(start)
    pos=[i,j]
    #All states are generated and the best one is picked and expanded thereafter 
    #in the next cycle 
    state.append(lefts(start,pos))
    state.append(rights(start,pos))
    state.append(ups(start,pos))
    state.append(downs(start,pos))
    notq = []
    for i in state:
        if i not in queue: #all those which have already been visited should not occur twice
            notq.append(i)
    if(len(notq)==0):
        return -1
    lismis=[]
    for i in notq:    #sorting on the basis of heurestic values
        lismis.append(misplaced(i))
        if misplaced(i)<=misplaced(start):
          return i

#This is a normal function to print the board like a matrix to make it look more 
#presentable.

def printboard_102003730(s):
    for i in s:
        for j in i:
            print(j,end=" ")
        print()
    print()

#This is the solver function which solves the problem for us taking the start 
#and end as the parameter 

def solver(final,start):
    global steps
    steps=0
    if(final==start):
        return final
    else:
        while(compare(start,final)==0):
            steps+=1
            printboard_102003730(start) #printing intermediate steps to the goal node
            queue.append(start)   #adding the visited nodes to the array for checking
            start = getminnewstates(start)
            if(start==-1):  #if no solution has been found in the search using heurestic
                print("No solution found")
                return -1
        return start
var = solver(goalSaloni,start)
if(var!=-1):
    printboard_102003730(var)
print("The total number of steps are: ",steps)