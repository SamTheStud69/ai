def uniformSearch(goal, start):
# minimum cost upto
# goal state from starting
  global graph_102003060, cost
  sol = []
#declare a priority queue and sol vector to max
  queue = []
  for i in range(len(goal)):
    sol.append(10 ** 8)
# insert the starting index
  queue.append([0, start])
# map to store visited node

  visited = {}
# count
  count = 0
# while the queue is not empty
  while (len(queue) > 0):
# get the top element of the
    queue = sorted(queue)
    p = queue[-1]
# pop the element
    del queue[-1]
# get the original value
    p[0] *= -1
# check if the element is part of
# the goal list
    if (p[1] in goal):
# get the position
      index = goal.index(p[1])
# if a new goal is reached
      if (sol[index] == 10 ** 8):
          count += 1
# if the cost is less
      if (sol[index] > p[0]):
          sol[index] = p[0]
# pop the element
      del queue[-1]
      queue = sorted(queue)
      if (count == len(goal)):
          return sol
# check for the non visited nodes
# which are adjacent to present node
    if (p[1] not in visited):
       for i in range(len(graph_102003060[p[1]])):
# value is multiplied by -1 so that
# least priority is at the top
           queue.append([(p[0] + cost[(p[1], graph_102003060[p[1]][i])]) * -1,graph_102003060[p[1]][i]])
# mark as visited
       visited[p[1]] = 1
    return sol
#Driver Code

# create the graph
graph_102003060, cost = [[] for i in range(8)], {}
#Adding edges
graph_102003060[0].append(1)
graph_102003060[0].append(3)
graph_102003060[3].append(1)
graph_102003060[3].append(6)
graph_102003060[3].append(4)
graph_102003060[1].append(6)
graph_102003060[4].append(2)
graph_102003060[4].append(5)
graph_102003060[2].append(1)
graph_102003060[5].append(2)
graph_102003060[5].append(6)
graph_102003060[6].append(4)
#Adding the cost
cost[(0, 1)] = 2
cost[(0, 3)] = 5
cost[(1, 6)] = 1
cost[(3, 1)] = 5
cost[(3, 6)] = 6
cost[(3, 4)] = 2
cost[(2, 1)] = 4
cost[(4, 2)] = 4
cost[(4, 5)] = 3
cost[(5, 2)] = 6
cost[(5, 6)] = 3
cost[(6, 4)] = 7
#Goal state
goal = []
#set the goal
goal.append(6)
# get the sol
sol = uniformSearch(goal, 0)
# print the sol
print("Minimum cost is = ", sol[0])