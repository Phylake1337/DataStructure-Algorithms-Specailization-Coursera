#Uses python3

import sys
import queue

def distance(adj, cost, s, t):
    disList = list(float("inf") for _ in range(len(adj)))
    disList[s] = 0
    #Min heap-based priority Qi
    Qi = queue.PriorityQueue()
    Qi.put((0, s))
    
    while not Qi.empty():
       V_Dis , V = Qi.get()
       
       if V == t : break
       for i,edge in enumerate(adj[V]):
           if disList[edge] > V_Dis + cost[V][i]:
               disList[edge] = V_Dis + cost[V][i]
               Qi.put((disList[edge], edge))
    
    if disList[t] == float("inf"):
        return -1
    return disList[t]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n + 1)]
    cost = [[] for _ in range(n + 1)]
    for ((a, b), w) in edges:
        adj[a].append(b)
        cost[a].append(w)
    s, t = data[0], data[1]
    print(distance(adj, cost, s, t))
