from copy import deepcopy as deepc

q = []
visited = []

def transfer01 (jug):
    j = deepc(jug)
    while (j[1] < 8 and j[0] > 0):
        j[1] += 1
        j[0] -= 1
    print("-------------------------------------------------------")
    print (j)
    return j

def transfer10 (jug):
    j = deepc(jug)
    while (j[0] < 12 and j[1] > 0):
        j[0] += 1
        j[1] -= 1
    print("-------------------------------------------------------")
    print (j)
    return j

def transfer12 (jug):
    j = deepc(jug)
    while (j[2] < 5 and j[1] > 0):
        j[2] += 1
        j[1] -= 1
    print("-------------------------------------------------------")
    print (j)
    return j

def transfer21 (jug):
    j = deepc(jug)
    while (j[1] < 8 and j[2] > 0):
        j[1] += 1
        j[2] -= 1
    print("-------------------------------------------------------")
    print (j)
    return j

def transfer02 (jug):
    j = deepc(jug)
    while (j[2] < 5 and j[0] > 0):
        j[2] += 1
        j[0] -= 1
    print("-------------------------------------------------------")
    print (j)
    return j

def transfer20 (jug):
    j = deepc(jug)
    while (j[0] < 12 and j[2] > 0):
        j[0] += 1
        j[2] -= 1
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
    j = [12,0,0]

    curr_j = deepc(j)

    while (1):
    
        new_j = transfer01(curr_j)
        if new_j[0] == 6:
            print(new_j)
            print("Found")
            exit()
        else:
            enqueue(new_j)
        print (q)

        new_j = transfer02(curr_j)
        if new_j[0] == 6:
            print(new_j)
            print("Found")
            exit()
        else:
            enqueue(new_j)
        print (q)
    
        new_j = transfer12(curr_j)
        if new_j[0] == 6:
            print(new_j)
            print("Found")
            exit()
        else:
            enqueue(new_j)
        print (q)

        new_j = transfer10(curr_j)
        if new_j[0] == 6:
            print(new_j)
            print("Found")
            exit()
        else:
            enqueue(new_j)
        print (q)

        new_j = transfer20(curr_j)
        if new_j[0] == 6:
            print(new_j)
            print("Found")
            exit()
        else:
            enqueue(new_j)
        print (q)
    
        new_j = transfer21(curr_j)
        if new_j[0] == 6:
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