def prettyfy(dict):
    for k, v in dict.items():
        print("smallest cost of distance from start node to {} is {}".format(k, v))

def shortestReach(n, edges, s): # takein number of nodes, all the edges in the given graph/s and a starting point s 
    seen = set() # this keeps track of the already seen nodes 
    paths_so_far = [] # keeps track of the path so far
    # To test if new node exists in paths_so_far

    # keeps track of  what is on the path so far, it is a set 
    #for easy access time instead of looping through the paths_so_far array which takes O(n)
    paths_so_far_set = set() 

    distances = {} #  this stores the distance from node s, the starting node up to the target nodes 
    
    # Initialize dict of nodes
    for node in range(1, n+1): # populate the nodes first 
        if node == s:
            distances[node] = 0 # distance from the starting node to its self is zero
        else:
            distances[node] = float('inf') # it is assumed the distance frm the start node to the target node is infinity at first
    
    current = s
    current_dist = 0
    # loop to ensure all the nodes we are traversing through have not been
    #  computed already to avoid dublicates
    while current not in seen:
        seen.add(current) # mark the current node as already seen
        for edge in edges: # loop though all the edges of the current not
            # Map the adjecent nodes from the current egde 
            if current == edge[0]:   neighbor = edge[1]
            elif current == edge[1]: neighbor = edge[0]
            else: continue
            # map the distance from the current distance to the next edge in the adjanceny list
            distance = current_dist + edge[2]
            # because we minimum distance appended we 
            #compare the computed distance to what we already had in memory 
            distances[neighbor] = min( distance, distances[neighbor])
            # add the new newighbou and distance to paths_so_far list of tupples if we had not come across the neighbor edge 
            if neighbor not in paths_so_far_set:
                paths_so_far.append((distance, neighbor))
                paths_so_far_set.add(neighbor) # add the neighbour to the set paths_so_far_set for easy look up in future 
        
        # sort the paths_so_far for mimic the min-priority queue, and we are sorting the the node numer
        paths_so_far = sorted(paths_so_far)
        current = paths_so_far.pop(0) 
        current, current_dist = current[1], current[0]
        paths_so_far_set.remove(current)
    
    del distances[s] # remove the start node becuase the node and distance are always zero
    for item in distances:
        if distances[item] == float('inf'): # check if there is a node that cant be reached from the start node, if so the node distance will still be infinity, because it wont have changes. 
            distances[item] = -1 # make it a -1 as required by instructions 
    prettyfy(distances) # prints a pretty version of the nodes and distances from the start 

    ouput  = []
    #returns a sorted list of distances as printed by the prettfy function 
    for node in sorted(distances): ouput.append(distances[node])
    return ouput

 

# This is taking in the inputs this script should be run on terminal and the should get a text file as an arguiment 
 

import sys
input  = open(sys.argv[1]) 
edges = []
for line in input:
    ln = line.split()
    if len(ln) == 2:
        Nodes = int(ln[0])
        Edges = int(ln[1])
    if len(ln) == 3:
        edges.append(list(map(int, line.rstrip().split())))
    if len(ln) == 1:
        start = int(ln[0])

result = shortestReach(Nodes, edges, start)
print(result)

