#Uses python3
import sys
import math
from queue import PriorityQueue

def getDis(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))

def closestPoint(v, spacePoints, visited, distance, Qi):
    origin = spacePoints[v]
    for i in range (len(spacePoints)):
        dis = getDis(origin, spacePoints[i])
        if dis < distance[i] and visited[i] == False:
            distance[i] = dis
            Qi.put((dis ,i))


def clustering(spacePoints):
    Qi = PriorityQueue()
    visited = list(False for _ in range(len(spacePoints)))
    distance = list(float("inf") for _ in range(len(spacePoints)))
    visited[0] = True
    distance[0] = 0
    Qi.put((distance[0] ,0))
    while not Qi.empty():
        _, v = Qi.get()
        visited[v] = True
        closestPoint(v, spacePoints, visited, distance, Qi)
    return min(sorted(distance, reverse = True)[:k-1])

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1:-1:2]
    y = data[2::2]
    k = data[-1]
    spacePoints = []
    for i in range(len(x)):
        spacePoints.append((x[i], y[i]))
    print("{0:.9f}".format(clustering(spacePoints)))
    