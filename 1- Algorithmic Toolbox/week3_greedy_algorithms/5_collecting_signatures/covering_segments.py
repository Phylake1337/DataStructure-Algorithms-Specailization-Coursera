# Uses python3
import sys

from collections import namedtuple
Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    i=1
    segments = sorted(segments)
    seg1, seg2 = segments[i-1], segments[i]
    intersection = seg1
    for i in range(2, len(segments)+1):
        if seg1.end >= seg2.start and seg1.end < seg2.end:
            intersection = Segment(seg2.start, seg1.end)
            seg1 = intersection 
            
        elif seg1.end >= seg2.start and seg1.end >= seg2.end:
            intersection = seg2
            seg1 = intersection
            
        else:
            points.append(seg1.end)
            seg1 = segments[i-1]
        
        if i == len(segments):
            points.append(seg1.end)
            return points
        else:
            seg2 = segments[i]

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
