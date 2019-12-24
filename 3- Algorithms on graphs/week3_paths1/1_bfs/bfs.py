#Uses python3

import sys
from queue import Queue

Qi = Queue()
def distance(adj, s, t):
    distance = [0] + list(-1 for _ in range(n))
    distance[s] = 0
    Qi.put(s)
    while not Qi.empty():
        currV = Qi.get()
        for edge in adj[currV]:
            if distance[edge] == -1:
                Qi.put(edge)
                distance[edge] = distance[currV] + 1
    return distance[t]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    s, t = data[2 * (m + 1):]
    data = data[2: 2 * (m + 1)]
    adj = [[] for _ in range(n + 1)]
    #Prepare adjcent list
    for ind in range(0, len(data) - 1, 2):
        adj[data[ind]].append(data[ind + 1])
        adj[data[ind + 1]].append(data[ind])
    print(distance(adj, s, t))
    
    