#!/bin/python3

import math
import os
import random
import re
import sys

def prettyfy(dict):
    for k, v in dict.items():
        print("smallest cost of distance from start node to {} is {}".format(k, v))

# Complete the shortestReach function below.
def shortestReach(n, edges, s):
    visited = set()
    frontier = []
    # To test if new node exists in frontier
    frontier_set = set()
    distances = {}
    
    # Initialize dict of nodes
    for node in range(1, n+1):
        if node == s:
            distances[node] = 0
        else:
            distances[node] = float('inf')
    
    current = s
    current_dist = 0
    
    while current not in visited:
        visited.add(current)
        for edge in edges:
            if current == edge[0]:
                neighbor = edge[1]
            elif current == edge[1]:
                neighbor = edge[0]
            else:
                continue
            distance = current_dist + edge[2]
            if distance < distances[neighbor]:
                distances[neighbor] = distance
            if neighbor not in frontier_set:
                frontier.append((distance, neighbor))
                frontier_set.add(neighbor)
        
        # Mimic a priority queue
        frontier = sorted(frontier)
                
        current = frontier.pop(0)
        current, current_dist = current[1], current[0]
        frontier_set.remove(current)
    
    del distances[s]
    for item in distances:
        if distances[item] == float('inf'):
            distances[item] = -1
    return distances
 




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
prettyfy(result)