#Assignment-3 Q5
import copy
#inputing the adjacency list and the cost of each edge in graph and saloni_cost itself
graph = {
  'S':['A','B','C'],
  'A':['G'],
  'B':['G'],
  'C':['G'],
  'G':[]
}
saloni_cost = {
  ('S','A'):1,
  ('S','B'):5,
  ('S','C'):15,
  ('A','G'):10,
  ('B','G'):5,
  ('C','G'):5,
}
saloni_totCost=0
temp=[]
saloni_paths=[]

def problem(node, end):
  global saloni_totCost, saloni_paths
  #checking if we have reached the end if yes than the path has been found 
  #it is pushed into the saloni_paths for analysis with the cost and 
  #the temp list is cleared for new input having only the starting node in it 
  if node==end:
    newpath=copy.deepcopy(temp)
    saloni_paths.append([saloni_totCost, newpath])
    temp.clear()
    temp.append('S')
    saloni_totCost=0
    return
  for neighbour in graph[node]:
    saloni_totCost+=saloni_cost[node, neighbour]
    temp.append(neighbour)
    #recursive call to find the end node
    problem(neighbour, end)
  #sorting on the basis of total cost of path
  saloni_paths.sort(key=lambda x:x[0])

temp.append('S')
#adding the starting node to the list

#function call
problem('S', 'G')

#printing the path and the cost stored in saloni_paths[0] as after sorting 
#it is the shortest and the first item is the cost and the second item is the path itself
for node in saloni_paths[0][1]:
  print(node+" ",end='')
print(' with cost=', saloni_paths[0][0])