import heapq

class Solution:
    def MST(self, points):
        n = len(points)
        if not n or not points:   return 0
        pq = []
        seen = [False] * n
        total = 0
        count = n - 1

        # Create a heap of all edges that start form position 1,
        # in  our case that 2ill be 0
        p1, p2 = points[0]
        for j in range(1, n):
            x2, y2 = points[j]
            cost = abs(p1 - x2) + abs(p2 - y2)
            edge = Edges(0, j, cost)
        
            pq.append(edge)
        
        # Convert pq to a heap.
        heapq.heapify(pq)

        seen[0] = True
        while pq and count > 0:
            edge = heapq.heappop(pq)
            point1 = edge.point1
            point2 = edge.point2
            cost = edge.cost
            if not seen[point2]:
                total += cost
                seen[point2] = True
                for j in range(n):
                    if not seen[j]:
                        distance = abs(points[point2][0] - points[j][0]) + \
                                   abs(points[point2][1] - points[j][1])
                        heapq.heappush(pq, Edges(point2, j, distance))
                count -= 1
        return total

class Edges:
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




