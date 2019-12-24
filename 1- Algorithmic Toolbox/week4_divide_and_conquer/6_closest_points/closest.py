# Uses python3
from itertools import combinations
from math import sqrt



def Distance_squared(first_point, second_point):
    return (first_point[0] - second_point[0]) ** 2 + (first_point[1] - second_point[1]) ** 2

def minimum_distance_squared(points):
    if len(points) == 2:
        return Distance_squared(points[0], points[1])
    
    if len(points) == 3:
        return min(Distance_squared(points[0], points[1]),
                   Distance_squared(points[0], points[2]),
                   Distance_squared(points[1], points[2]))
    
    def funY (x):
        return x[1]
    
    pointsX = sorted(points)
    
    mid = len(points) // 2
    midPoint = pointsX[mid-1][0] + (pointsX[mid][0] - pointsX[mid - 1][0]) / 2 
    
    d1 = minimum_distance_squared(pointsX[ : mid])
    d2 = minimum_distance_squared(pointsX[mid  : ])
    
    d = min(d1, d2)
    stripRange = [midPoint - d, midPoint + d]
    
    stripPoints = []
    for point in pointsX:
        if stripRange[0] <= point[0] <= stripRange[1]:
            stripPoints.append(point)
    
    stripPoints = sorted(stripPoints, key = funY)
    dStrip = float("inf")
    for i in range(len(stripPoints)):
        for j in range(i+1, min(i+5, len(stripPoints))):
            p1, p2  = stripPoints[i], stripPoints[j]
            dStrip = min(dStrip, Distance_squared(p1,p2))
                
    return min(d, dStrip)        


if __name__ == '__main__':
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = (x, y)
        input_points.append(input_point)

    print("{0:.9f}".format(sqrt(minimum_distance_squared(input_points))))
