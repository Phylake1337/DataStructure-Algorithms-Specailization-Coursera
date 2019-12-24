# python3

import sys

def explore(v):    
    if not visited[v]:
        visited[v] = True
        
        for w in adj[v]:
            if not visited[w]: explore(w)
            
    
def number_of_components(adj):
    result = 0
    while False in visited:
        v = visited.index(False)
        explore(v)  
        result += 1
        
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    adj = [[] for _ in range(n + 1)]
    visited = [True] + list(False for _ in range(n))
    
    for ind in range(0, len(data) - 1, 2):
        adj[data[ind]].append(data[ind + 1])
        adj[data[ind + 1]].append(data[ind])
    
    print(number_of_components(adj))

