unvisited = [1,2,3,4]
dist = {1:[0,10,15,20], 2:[10,0,35,25], 3:[15,35,0,30], 4:[20,25,30,0]}

def shortest(beg, start):
    print(beg)
    unvisited.remove(beg)
    n = 0
    length = 0
    maxim = max(dist[beg])
    for i in unvisited: 
        if (dist[beg][i-1] <= maxim and dist[beg][i-1] != 0):
            maxim = dist[beg][i-1]
            n = i

    if (n != 0):
        length = dist[beg][n-1]

    if unvisited:
        length += shortest(n, start)
    else:
        length += dist[beg][start-1]
    return length

def main():
    start = int(input("Enter the Starting Node: "))
    
    print("Shortest Path = ", shortest(start, start))

if __name__ == '__main__':
    main()