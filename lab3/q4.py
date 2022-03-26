#Manhattan Distance is used as heuristic function
import copy

q = []
vis_102003060 = []

#Compares Start and Goal State
def compare(s, g):
    if s == g:
        return (1)
    else:
        return (0)

#Finds position of empty tile
def find_pos(s):
    for i in range(3):
        for j in range(3):
            if s[i][j] == 0:
                return ([i, j])

#Movement for the empty tile
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
    d = (s, g)
    print 
    d
# d = 0
# for i in range(3):
# for j in range(3):
# if s[i][j] != g[i][j]:
# d += 1
    return d
def dequeue(g):
    global q
    global vis_102003060
    q.sort()
    vis_102003060 = vis_102003060 + [q[0][1]]
    elem = q[0][1]
    del q[0]
    return (elem)

#Checks whether Goal State Can be achieved or not
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
