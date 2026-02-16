import heapq
import time
import numpy as np
import matplotlib.pyplot as plo
import os

def plotData(data):
    #loads the dataset txt file name 
    sel = np.loadtxt(data)
    #plot calculations
    x = data[:,0]
    y = data[:,1]
    plo.plot(x,y)
    plo.show()

def main():

    source =[]
    goal = []
    plotData('TSP1.txt')

if __name__ == "__main__":
    main()