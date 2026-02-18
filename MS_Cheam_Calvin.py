import heapq
import time
import numpy as np
import matplotlib.pyplot
import os

def ms_sq_generator():
    # create a 1-9 arr, shuffle order flattening after for easy work
    sq=np.array([1,2,3,4,5,6,7,8,9])
    np.random.shuffle(sq)
    return tuple(sq)

def check_neighbors(current_state):
    #check for each possible swap by swapping the r and d tiles of any given one
    neighbors =[]
    #flatten into single list if not already so
    states=list(current_state)
    #check all items
    for i in range(3):
        for j in range(3):
            #ind is value under current item
            ind = i*3+j
            #check R swap
            if j < 2:
                new_states =states[:]
                new_states[ind], new_states[ind+1] = new_states[ind+1], new_states[ind]
                neighbors.append(tuple(new_states))
            #check D swap
            if i < 2:
                new_states =states[:]
                new_states[ind], new_states[ind+3] = new_states[ind+3], new_states[ind]
                neighbors.append(tuple(new_states))
    return neighbors

def manhattan_h(state, goal):
    # calculate distance to goal, using dict for easy lookup
    dist = 0
    goal_p = {val:(i//3,i%3) for i,val in enumerate(goal)}
    for i,val in enumerate(state):
        cr,cc = i//3,i%3
        gr,gc=goal_p[val]
        dist += abs(cr-gr) +abs(cc-gc)
    return dist/2

def a_star_search(start,goal):
    start_time = time.time()
    visited={start:0}
    expanded_node=0
    q=[(manhattan_h(start, goal),0,start)]
    while q:
        #lowest score
        f,c,current = heapq.heappop(q)
        expanded_node +=1
        if current==goal:
            finish= time.time()-start_time
            return expanded_node,finish, c
        #check 1 swap possibilities
        for neighbor in check_neighbors(current):
            nl = c + 1
            if neighbor not in visited or nl <visited[neighbor]:
                visited[neighbor] = nl
                h = manhattan_h(neighbor, goal)
                #update new f=g+h
                heapq.heappush(q, (nl + h, nl, neighbor))

    return expanded_node, time.time()-start_time, -1
   

def ucs_search(start,goal):
    start_time = time.time()
    visited={start:0}
    expanded_node=0
    #queue of cost and current state
    q = [(0,start)]

    while q:
        c, current = heapq.heappop(q)
        expanded_node += 1

        if current == goal:
            finish = time.time() - start_time
            return expanded_node, finish, c
            
        # Check all neighbors in next swap
        for neighbor in check_neighbors(current):
            nl = c + 1
            if neighbor not in visited or nl < visited[neighbor]:
                visited[neighbor] = nl
                # priority is path cost (nl)
                heapq.heappush(q, (nl, neighbor))
    return expanded_node, time.time() - start_time, -1

def main():
    source =ms_sq_generator()
    goal = (8,1,6,3,5,7,4,9,2)
    Nodes,finishT,cost=a_star_search(source,goal)
    UCSnode,UCSfinishT,UCScost=ucs_search(source,goal)
    print(f'{np.array(source).reshape((3, 3))}')
    print(f'A* Search')
    print(f'Swaps:{cost}')
    print(f'Time taken:{finishT}')
    print(f'Nodes visited: {Nodes}')
    print(f'UCS Search')
    print(f'Swaps:{UCScost}')
    print(f'Time taken:{UCSfinishT}')
    print(f'Nodes visited: {UCSnode}')
    
    
    

if __name__ == "__main__":
    main()
