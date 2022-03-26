from copy import deepcopy

class pair:
    def init(self,below,block):
        self.below = below
        self.block = block

# Returns the map of level vs list of block at that level (used to cal heuristic value)
def stateLevelMap(state):     
    levelMap = {-1: [None] ,0:[],1:[],2:[],3:[]}
    for i in range(4):
        if(len(levelMap[i-1])==0):
            break
        for p in state:
            if p.below in levelMap[i-1]:
                levelMap[i].append(p.block)
    return levelMap

# Returns block below
def getBelow(state,block):     
    if(block == None):
        return None
    for p in state:
        if(p.block == block):
            return p.below

# Returns Heuristic Value
def heuristic(state,goal):      
                               
    state_level  = stateLevelMap(state)
    goal_level = stateLevelMap(goal)
    h = 0
    for i in range(1,len(state)):   
        if(len(state_level[i])>0 and len(goal_level[i])>0):
            for block in state_level[i]:
                if block in goal_level[i]:
                    bi = block
                    bg = bi
                    add = True
                    for k in range(i,0,-1):
                        bi = getBelow(state,bi)
                        bg = getBelow(goal,bg)
                        if(bi!=bg):
                           h -= i
                           add = False
                           break
                    if(add):
                        h += i
                else:
                    h -= i
        elif(len(state_level[i])!= 0):
            h -= i
        else:
            return h
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
    max_heu = heuristic(init,goal)
    ret_state = init
    top = topBlock(state)
    # n^2 move n = len(top)
    for i in range(len(top)):
        for j in range(len(top)):   
            if( i == j ):       # place ith block on ground
                update(state,pair(None,top[i]))
                h_val = heuristic(state,goal)
                if(h_val>=max_heu):
                    max_heu = h_val
                    ret_state = deepcopy(state)
                state = deepcopy(init)
            else:                # place the ith block on top of jth block
                update(state,pair(top[j],top[i]))
                h_val = heuristic(state,goal)
                if(h_val>=max_heu):
                    max_heu = h_val
                    ret_state = deepcopy(state)
                state = deepcopy(init)
    if (ret_state == init):
        return None             
    return ret_state   


# Prints State
def printState(state): 
    for p in state:
        print((p.below,p.block),end=', ')
    print()
        
# Solution Function
def solve(init,goal):       
    steps = 0
    state = deepcopy(init)
    goal_heu = heuristic(goal,goal)
    while(state!=None):
        printState(state)
        if(heuristic(state,goal)==goal_heu):
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