#Number of misplaced tiles is used as heuristic function and Best first Search Algorithm is used

import sys
import copy
q = []
vis_102003060 = []

#To compare the start and goal State
def compare(s, g):
    if s == g:
     return (1)
    else:
     return (0)

#To find the pos of empty tile
def find_pos(s):
   for i in range(3):
    for j in range(3):
      if s[i][j] == 0:
        return ([i, j])


#Movement of empty tile
def up(s, pos):
    i = pos[0]
    j = pos[1]
    if i > 0:
        temp = copy.deepcopy(s)
        temp[i][j] = temp[i - 1][j]
        temp[i - 1][j] = 0
        return (temp)
    else:
        return (s)

def down(s, pos):
    i = pos[0]
    j = pos[1]
    if i < 2:
        temp = copy.deepcopy(s)
        temp[i][j] = temp[i + 1][j]
        temp[i + 1][j] = 0
        return (temp)
    else:
        return (s)
def right(s, pos):
    i = pos[0]
    j = pos[1]
    if j < 2:
        temp = copy.deepcopy(s)
        temp[i][j] = temp[i][j + 1]
        temp[i][j + 1] = 0
        return (temp)
    else:
        return (s)
def left(s, pos):
    i = pos[0]
    j = pos[1]
    if j > 0:
        temp = copy.deepcopy(s)
        temp[i][j] = temp[i][j - 1]
        temp[i][j - 1] = 0
        return (temp)
    else:
        return (s)

def enqueue(s, val):
    global q
    q = q + [(val, s)]
def heuristic(s, g):
    d = 0
    for i in range(3):
        for j in range(3):
            if s[i][j] != g[i][j]:
                d += 1
    print(d)
    return d
def dequeue(g):
    global q
    global vis_102003060
    q.sort()
    vis_102003060 = vis_102003060 + [q[0][1]]
    elem = q[0][1]
    del q[0]
    return (elem)

#Whether goal state can be achieved or not 
def search(s, g):
    curr_state = copy.deepcopy(s)
    if s == g:
        return
    global vis_102003060
    while (1):
        pos = find_pos(curr_state)
        new = up(curr_state, pos)
        if new != curr_state:
            if new == g:
                print("Goal State achieved with intermediate states as:")
                print(vis_102003060 + [g])
                return
            else:
                if new not in vis_102003060:
                    enqueue(new, heuristic(new, g))
        new = down(curr_state, pos)
        if new != curr_state:
            if new == g:
                print("Goal State achieved with intermediate states as:")
                print(vis_102003060 + [g])
                return
            else:
                if new not in vis_102003060:
                    enqueue(new, heuristic(new, g))
        new = right(curr_state, pos)
        if new != curr_state:
            if new == g:
                print("Goal State achieved with intermediate states as:")
                print(vis_102003060 + [g])
                return
            else:
                if new not in vis_102003060:
                    enqueue(new, heuristic(new, g))
        new = left(curr_state, pos)
        if new != curr_state:
            if new == g:
                print("Goal State achieved with intermediate states as:")
                print(vis_102003060 + [g])
                return
            else:
                if new not in vis_102003060:
                    enqueue(new, heuristic(new, g))
        if len(q) > 0:
            curr_state = dequeue(g)
        else:
            print("Couldn't find")
            return
#Driver Code
def main():
 s = [[2, 0, 3], [1, 8, 4], [7, 6, 5]]
 g = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
 global q
 global vis_102003060
 q = q
 vis_102003060 = vis_102003060 + [s]
 search(s, g)

main()