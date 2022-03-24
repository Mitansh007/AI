import copy
import numpy as np

q = []
visited = []

def compare(s0, g):
    if np.all(s0 == g):
        return 1
    else:
        return 0

def findPos(s):
    for i in range (len(s)):
        for j in range (len(s[0])):
            if s[i][j] == 0:
                return [i,j]

def up(s, pos):
    row = pos[0]
    col = pos[1]
    s1 = copy.deepcopy(s)
    if row == 0:
        return s1
    else:
        s1[row][col], s1[row-1][col] = s1[row-1][col], s1[row][col]
        print("---------------------------------------------------------")
        print(s1)
        return s1

def down(s,pos):
    row = pos[0]
    col = pos[1]
    s1 = copy.deepcopy(s)
    if row == (len(s1) - 1):
        return s1
    else:
        s1[row][col], s1[row+1][col] = s1[row+1][col], s1[row][col]
        print("---------------------------------------------------------")
        print(s1)
        return s1

def left(s,pos):
    row = pos[0]
    col = pos[1]
    s1 = copy.deepcopy(s)
    if col == 0:
        return s1
    else:
        s1[row][col], s1[row][col-1] = s1[row][col-1], s1[row][col]
        print("---------------------------------------------------------")
        print(s1)
        return s1

def right(s,pos):
    row = pos[0]
    col = pos[1]
    s1 = copy.deepcopy(s)
    if col == (len(s1[row]) - 1):
        return s1
    else:
        s1[row][col], s1[row][col+1] = s1[row][col+1], s1[row][col]
        print("---------------------------------------------------------")
        print(s1)
        return s1

def enqueue(s):
    flag = 0
    for i in visited:
        if compare(i, s):
            flag = 1
            break
    if flag == 0:
        q.append(s)

def dequeue():
    if (len(q)==0):
        print("Goal can't be reached")
        exit()
    else:
        return q.pop(0)

def main():
    s0 = np.array([[1,2,3], [8,0,4], [7,6,5]])
    g = np.array([[2,8,1], [0,4,3], [7,6,5]])

    curr_state = copy.deepcopy(s0)

    while (1):
        pos = findPos(curr_state)
        # print (pos)
        

        new_state = up(curr_state, pos)
        if compare(new_state, g) == 1:
            print("Found")
            exit()
        else:
            enqueue(new_state)
        
        new_state = down(curr_state,pos)
        if compare(new_state, g) == 1:
            print("Found")
            exit()
        else:
            enqueue(new_state)
        
        new_state = right(curr_state,pos)
        if compare(new_state, g) == 1:
            print("Found")
            exit()
        else:
            enqueue(new_state)
        
        new_state = left(curr_state,pos)
        if compare(new_state, g) == 1:
            print("Found")
            exit()
        else:
            enqueue(new_state)

        visited.append(curr_state)
        curr_state = dequeue()
        print("---------------------------------------------------------")
    
    

if __name__ == '__main__':
    main()