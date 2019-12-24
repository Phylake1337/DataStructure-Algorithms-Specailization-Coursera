#Uses python3

import sys

def DFS(used, order, v):
    if used[v]:
        return
    
    if adj[v] == []:
        used[v] = True
        order.append(v)
    else:    
        for w in adj[v]:
            DFS(used, order, w)
        used[v] = True
        order.append(v)            

        
def toposort(adj):
    used = [True] + list(False for _ in range(n))
    order = []
    s = 0
    while True:
        try:
            s = used.index(False, s)
            DFS(used, order, s) 
        except:
            break
    order = reversed(order)
    return order


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    adj = [[] for _ in range(n + 1)]
    
    for ind in range(0, len(data) - 1, 2):
        adj[data[ind]].append(data[ind + 1])
        
    order = toposort(adj)
    for x in order:
        print(x , end=' ')