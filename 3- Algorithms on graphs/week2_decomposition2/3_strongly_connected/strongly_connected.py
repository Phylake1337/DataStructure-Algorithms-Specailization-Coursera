#Uses python3

import sys
sys.setrecursionlimit(200000)

def reverse(adj):
    newAdj = list([] for _ in range(len(adj)))
    for i, vertecies in enumerate(adj):
        for vertex in vertecies:
            newAdj[vertex].append(i)
    return newAdj

def DFS(adj, used, order, v):
    if used[v]:
        return
    else:
        used[v] = True
        
    for w in adj[v]:
        DFS(adj, used, order, w)
    
    order.append(v)            

def getPostVertcies(adj):
    order = []
    used = [True] + list(False for _ in range(n))
    s = 0
    while True:
        try:
            s = used.index(False, s)
            DFS(adj, used, order, s)
        except:
            break
    return order

def number_of_strongly_connected_components(adj):
    result = 0
    explore_visited = [True] + list(False for _ in range(n))
    #get Reverse Graph
    reversedAdj = reverse(adj)
    #get the list of ordered postorder vertecies
    postVertecies = getPostVertcies(reversedAdj)
    while postVertecies:
        v = postVertecies.pop()
        if not explore_visited[v]:
            #explore the sink and mark vetecies in SCC
            DFS(adj, explore_visited, [], v)
            result += 1
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    adj = [[] for _ in range(n + 1)]
    
    for ind in range(0, len(data) - 1, 2):
        adj[data[ind]].append(data[ind + 1])
        

    print(number_of_strongly_connected_components(adj))