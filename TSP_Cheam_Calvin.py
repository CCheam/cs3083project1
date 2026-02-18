import heapq
import time
import numpy as np
import matplotlib.pyplot as plo
import os


def txtToArr(file):
    #load txt into an int arr
    data = np.loadtxt(file,dtype=int)
    return data

def plotData(data):
    #loads the dataset txt file name 
    #sel = np.loadtxt(data)
    #plot calculations
    #x = data[,0]
    #y = data[,1]
    #plo.plot(x,y,marker='o')
    plo.show()

def BF_TSP():

    return ()

def SA_TSP():
    return()

def main():
    print(txtToArr('TSP1.txt'))

if __name__ == "__main__":
    main()