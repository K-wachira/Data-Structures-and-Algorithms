import heapq
class Solution:
    def minCostConnectPoints(self, points):
        if not points or len(points) == 0:
            return 0
        size = len(points)
        pq = []
        visited = set()
        result = 0
        count = size - 1
        # Add all edges from points[0] vertexs
        # x1, y1 = points[0]
        # for j in range(1, size):
        #     # Calculate the distance between two coordinates.
        #     cost= points[j][2]
        #     # cost = abs(x1 - x2) + abs(y1 - y2)
        #     edge = Edge(0, j, cost)
        #     pq.append(edge)
        
        # for item in points:
        #     start = item[0]
        #     end = item[1]
        #     weight = item[2]
        #     edge = Edge( start, end, weight)
        #     pq.append(edge)

        pq = [Edge(points[0], points[1], points[2])]
        # Convert pq to a heap.
        heapq.heapify(pq)
        for i in range(len(pq)):
            print(pq[i].point1, pq[i].point2, pq[i].cost)

        
        while pq and count > 0:
            edge = heapq.heappop(pq)
            point1 = edge.point1
            point2 = edge.point2
            visited.add(point1)
            cost = edge.cost
            if point 2 not in visited:
                result += cost
                visited.add(point2)

                for item in points:
                    

                
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
    

points = [
[6, 1, 10],
[6, 5, 25],
[5, 7, 24],
[5, 4, 22],
[7, 2, 14], 
[7, 4, 18],
[4, 3, 12],
[3, 2, 16],
[1, 2, 28]
]

# points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
solution = Solution()
print(f"points = {points}")
print(f"Minimum Cost to Connect Points = {solution.minCostConnectPoints(points)}")