from copy import deepcopy as deepc

q = []
visited = []

def fill (jug, n):
    j = deepc(jug)
    if n == 0:
        if (j[n] < 4):
            j[n] = 4
    else:
        if (j[n] < 3):
            j[n] = 3
    print("-------------------------------------------------------")
    print (j)
    return j

def empty (jug, n):
    j = deepc(jug)
    if (j[n] > 0):
        j[n] = 0
    print("-------------------------------------------------------")
    print (j)
    return j

def transfer01 (jug):
    j = deepc(jug)
    while (j[1] < 3 and j[0] > 0):
        j[1] += 1
        j[0] -= 1
    print("-------------------------------------------------------")
    print (j)
    return j

def transfer10 (jug):
    j = deepc(jug)
    while (j[0] < 4 and j[1] > 0):
        j[0] += 1
        j[1] -= 1
    print("-------------------------------------------------------")
    print (j)
    return j

def enqueue(state):
    flag = 0
    for i in visited:
        if i == state:
            flag = 1
            break
    if flag == 0:
        q.append(state)

def dequeue():
    if (len(q) == 0):
        print("Goal can't be reached")
        exit()
    else:
        return q.pop(0)

def main ():
    j = [0,0]
    goal = [2,0]

    curr_j = deepc(j)

    while (1):
        
        new_j = fill(curr_j, 0)
        if new_j == goal:
            print(new_j)
            print("Found")
            exit()
        else:
            enqueue(new_j)
        print (q)

        new_j = fill(curr_j, 1)
        if new_j == goal:
            print(new_j)
            print("Found")
            exit()
        else:
            enqueue(new_j)
        print (q)

        visited.append([0,0])
        visited.append(curr_j)
        curr_j = dequeue()
        print("-------------------------------------------------------")

        if (curr_j[0] > curr_j[1]):
            new_j = transfer01(curr_j)
            if new_j == goal:
                print(new_j)
                print("Found")
                exit()
            else:
                enqueue(new_j)
            print (q)
        else:
            new_j = transfer10(curr_j)
            if new_j == goal:
                print(new_j)
                print("Found")
                exit()
            else:
                enqueue(new_j)
            print (q)
        
        new_j = empty(curr_j, 0)
        if new_j == goal:
            print(new_j)
            print("Found")
            exit()
        else:
            enqueue(new_j)
        print (q)
        
        new_j = empty(curr_j, 1)
        if new_j == goal:
            print(new_j)
            print("Found")
            exit()
        else:
            enqueue(new_j)
        print (q)

        visited.append(curr_j)
        curr_j = dequeue()
        print("-------------------------------------------------------")



if __name__ == '__main__':
    main()