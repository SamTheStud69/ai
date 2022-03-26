from copy import deepcopy

class pair:
    def init(self,below,block):
        self.below = below
        self.block = block

# Returns Heuristic Value
def heuristic(state,goal): 
    h = 0                 
    for x in state:        # Loops through all pairs in state          
        for y in goal:     # Loops through all pair in goal
            if(x.block == y.block):
                if(x.below == y.below):   #if on the right block h = +1
                    h +=1
                else:
                    h -= 1     #else h = -1          
                break
    return h

# Returns TopMost Block
def topBlock(state):          
    top = ['A','B','C','D']
    for pair in state:
        if pair.below in top:
            top.remove(pair.below)
    return top

# Adds new pos of block and removes previous position
def update(state,entry):    
    for p in state:
        if(p.block == entry.block):
            state.remove(p)
            state.append(entry)
            return

# Returns the Step with more heuristic value than init
def move(init,goal):        
    state = deepcopy(init)
    heu = heuristic(init,goal)
    top = topBlock(state)
    # n^2 moves n = len(top)
    for i in range(len(top)):
        for j in range(len(top)):   
            if( i == j ):   # place ith block on ground
                update(state,pair(None,top[i]))
                if(heuristic(state,goal)>heu):
                    return state
                state = deepcopy(init)
            else:           # place the ith block on top of jth block
                update(state,pair(top[j],top[i]))
                if(heuristic(state,goal)>heu):
                    return state
                state = deepcopy(init)
    return None     


# Prints 'State' array
def printState(state):     
    for p in state:
        print((p.below,p.block),end=', ')
    print()
        
# Solution Function
def solve(init,goal):       
    steps = 0
    state = deepcopy(init)
    while(state!=None):
        printState(state)
        if(heuristic(state,goal)==len(state)):
            print('Hill Climbing Algo Successfull')
            print('Intermediate Steps:',steps)
            return
        else:
            state = move(state,goal)
        steps +=1
    print('Hill Climbing Algo Unsuccessfull!')
    return
            
# Driver Code
init = [pair(None,'B'),pair('B','C'),pair('C','D'),pair('D','A')]
goal = [pair(None,'A'),pair('A','B'),pair('B','C'),pair('C','D')]
solve(init,goal)