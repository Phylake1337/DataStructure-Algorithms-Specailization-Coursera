# python3

import sys

def explore(v):
    global found
    global visited
    
    if found == 1:
        return 
    
    if not visited[v]:
        visited[v] = True
        for w in adj[v]:
            if not visited[w]:
                if w == y:
                    found = 1
                    return
                else:
                    explore(w)
    
    
def reach(adj, x, y):
    explore(x)
    
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    x, y = data[2 * (m + 1):]
    data = data[2: 2 * (m + 1)]
    adj = [[] for _ in range(n + 1)]
    visited = list(False for _ in range(n + 1))
    found = 0
    #Prepare adjcent list
    for ind in range(0, len(data) - 1, 2):
        adj[data[ind]].append(data[ind + 1])
        adj[data[ind + 1]].append(data[ind])
    
    reach(adj, x, y)
    print(found)


