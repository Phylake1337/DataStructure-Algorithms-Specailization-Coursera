#Uses python3

import sys

def relax(adj, cost, disList):
    relaxFlag = 0
    for V in range(1, len(adj)):
        V_Dis = disList[V]
        for i,edge in enumerate(adj[V]):
           if disList[edge] > V_Dis + cost[V][i]:
               disList[edge] = V_Dis + cost[V][i]
               relaxFlag = 1
    return disList, relaxFlag

def negative_cycle(adj, cost):
    Vdist = list(pow(10,10) for _ in range(len(adj)))
    Vdist[1] = 0
    for _ in range(len(adj) - 1):
        Vdist, _ = relax(adj, cost, Vdist)
    #relax one more time to check negative cycle
    Vdist, relaxFlag = relax(adj, cost, Vdist)
    return relaxFlag


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
    print(negative_cycle(adj, cost))