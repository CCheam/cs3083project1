import heapq
import time
import numpy as np
import matplotlib.pyplot
import os

def ms_sq_generator():
    sq=np.array([1,2,3,4,5,6,7,8,9])
    np.random.shuffle(sq)
    ans=sq.reshape((3,3))
    print(ans)

def main():

    source =ms_sq_generator()
    goal = [[8,1,6], 
            [3,5,7],
            [4,9,2]
            ] 
    

if __name__ == "__main__":
    main()
