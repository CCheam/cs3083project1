**Task 1**
I implemented my A* search by having it loop through tuples of heuristic distance, cost, and the current state. If it hasn't tested a combination or the action will bring the heuristic closer to the goal, then it will update the associated values. I decided on Manhattan Distance as it is easy to calculate and does not have to take diagonals into account like other methods. The function for it will loop through the array, calculating the combined distance for each element. The /2 accounts for 2 tiles changing positions for the cost of 1 movement. I don't know how to fit a table in markdown, so I will include an example of the metrics of each when the code is run with the start array included. What's interesting is that each method comes to the same movement strategy, but UCS both searches far more nodes and takes longer. 

[[7 5 3]
 [2 6 8]
 [1 9 4]]
A* Search
Swaps:12
Time taken:0.11117935180664062
Nodes visited: 3927
UCS Search
Swaps:12
Time taken:3.3524584770202637
Nodes visited: 351817

**Task 2**


**Task 3**
