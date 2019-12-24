# python3

import sys

def explore(v, adj):
    global cyc
    global visited
    
    if visited[v]:
        return
    
    if not marked[v]:
        marked[v] = True
    else:
        cyc = 1
        return
    
    for w in adj[v]:
        explore(w, adj)
        
    visited[v] = True 
    marked[v] = False
 

def acyclic(adj):
    for v in range(1, len(adj)):
        if cyc != 0:
            break
        explore(v, adj)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    adj = [[] for _ in range(n + 1)]
    visited = [True] + list(False for _ in range(n))
    marked = [True] + list(False for _ in range(n))
    cyc = 0
    
    for ind in range(0, len(data) - 1, 2):
        adj[data[ind]].append(data[ind + 1])

    acyclic(adj)
    print(cyc)
