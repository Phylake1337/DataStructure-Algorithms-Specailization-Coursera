# python3
import sys

def compute_min_refills(distance, tank, stops):
    #Check distance between stops
    stops = [0] + stops + [distance]
    for i in range (1, len(stops)):
        if stops[i] - stops[i-1] > tank:
            return -1
    #Otherwise Calculate the output
    stopNum = 0
    travelDis = 0
    s = 0
    e = 1
    while travelDis < distance:
        while stops[s] + m >= stops[e]:
            e += 1
            if stops[s] + m >= stops[-1]:
                return stopNum           
        s = e - 1
        stopNum += 1
        travelDis = stops[s]
        
    return stopNum


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
