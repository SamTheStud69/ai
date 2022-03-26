#Number of misplaced tiles is used as the heuristic function
import sys
import copy
curr_min = sys.maxsize
q = []
vis_102003060 = []

#To compare Start and Goal State
def compare(s, g):
    if s == g:
        return (1)
    else:
        return (0)

#Find postion of empty tile
def find_pos(s):
    for i in range(len(s)):
        for j in range(len(s[0])):
            if s[i][j] == 0:
                return ([i, j])

#Used to move the empty tile
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
def enqueue(s):
    global q
    q = q + [s]
def heuristic(s, g):
    d = 0
    for i in range(len(s)):
        for j in range(len(s[0])):
            if s[i][j] != g[i][j]:
                d += 1
    return d
def dequeue(g):
    h = []
    global q
    global vis_102003060
    global curr_min
    for i in range(len(q)):
        h = h + [heuristic(q[i], g)]
    if min(h) < curr_min:
        curr_min = min(h)
        index = h.index(min(h))
        vis_102003060 = vis_102003060 + [q[index]]
    else:
        print("Intermediate states are for optimal solution are:")
        print(vis_102003060)
        exit()
    elem = q[index]
    q = []
    return (elem)

#Checks whether goal state can be achieved or not
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
                    enqueue(new)
        new = down(curr_state, pos)
        if new != curr_state:
            if new == g:
                print("Goal State achieved with intermediate states as:")
                print(vis_102003060 + [g])
                return
            else:
                if new not in vis_102003060:
                    enqueue(new)
        new = right(curr_state, pos)
        if new != curr_state:
            if new == g:
                print("Goal State achieved with intermediate states as:")
                print(vis_102003060 + [g])
                return
            else:
                if new not in vis_102003060:
                    enqueue(new)
        
        new = left(curr_state, pos)
        if new != curr_state:
            if new == g:
                print("Goal State achieved with intermediate states as:")
                print(vis_102003060 + [g])
                return
            else:
                if new not in vis_102003060:
                    enqueue(new)
        if len(q) > 0:
            curr_state = dequeue(g)
        else:
            print("Couldn't find")
            return

#Driver Code
def main():
    s = [[2, 8, 3], [1, 5, 4], [7, 6, 0]]
    g = [[1, 2, 7], [8, 0, 5], [3, 4, 6]]
    global q
    global vis_102003060
    q = q + [s]
    vis_102003060 = vis_102003060 + [s]
    search(s, g)
main()
