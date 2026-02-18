import heapq
import time
import numpy as np
import matplotlib.pyplot
import os

def ms_sq_generator():
    # create a 1-9 arr, shuffle order and set it as 3 by 3 arr like goal
    sq=np.array([1,2,3,4,5,6,7,8,9])
    np.random.shuffle(sq)
    ans=sq.reshape((3,3))

def check_neighbors(current_state):
    neighbors =[]
    #flatten into single list
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

def a_star_search():
    return 
def main():

    source =ms_sq_generator()
    goal = [[8,1,6], 
            [3,5,7],
            [4,9,2]
            ] 
    

if __name__ == "__main__":
    main()
