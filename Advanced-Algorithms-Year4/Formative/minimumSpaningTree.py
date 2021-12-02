import heapq

class Solution:
    def MST(self, points):
        if not points or len(points) == 0:
            return 0
        size = len(points)
        pq = []
        visited = [False] * size
        result = 0
        count = size - 1
        # Add all edges from points[0] vertexs
        x1, y1 = points[0]
        for j in range(1, size):
            # Calculate the distance between two coordinates.
            x2, y2 = points[j]
            cost = abs(x1 - x2) + abs(y1 - y2)
            edge = Edge(0, j, cost)
        
            pq.append(edge)
        
        # Convert pq to a heap.
        heapq.heapify(pq)

        visited[0] = True
        while pq and count > 0:
            edge = heapq.heappop(pq)
            point1 = edge.point1
            point2 = edge.point2
            cost = edge.cost
            if not visited[point2]:
                result += cost
                visited[point2] = True
                for j in range(size):
                    if not visited[j]:
                        distance = abs(points[point2][0] - points[j][0]) + \
                                   abs(points[point2][1] - points[j][1])
                        heapq.heappush(pq, Edge(point2, j, distance))
                count -= 1
        return result

class Edge:
    def __init__(self, point1, point2, cost):
        self.point1 = point1
        self.point2 = point2
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost
    

points1 = [[0,0],[2,2],[3,10],[5,2],[7,0]]
points2 = [] 

solution1 = Solution()
total1 = solution1.MST(points1)


solution2 = Solution()
total2 = solution2.MST(points2)


# Testing 
# Case 1 
if total1 == 20:
    print("Running Test case 1")
    print("Test case 1 passed having returned 20 cost of the MST tree for this graph : ", end=" ")
    print("\n    :", points1)
else:
    print("Test case 1 Failed")
#Case 2
# if matchingSocks(array2) == 36:
#     print("Running Test case 1")
#     print("Test case 2 passed having returned {36} pairs")
# else:
#     print("Test case 2 Failed")




