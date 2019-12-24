#Uses python3

import sys
from queue import Queue

def colorConvert(color):
    if color == "black":
        return "white"
    else:
        return "black"
    
Qi = Queue()
def bipartite(adj):
    vertexColor = ["grey"] + list("grey" for _ in range(n))
    vertexColor[1] = "black"
    Qi.put(1)
    bipartite = 1
    while not Qi.empty() and bipartite:
        currV = Qi.get()
        for edge in adj[currV]:
            if vertexColor[edge] == "grey":
                Qi.put(edge)
                vertexColor[edge] = colorConvert(vertexColor[currV])
            else:
                if vertexColor[edge] == vertexColor[currV]:
                    bipartite = 0
                    break
    return bipartite


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2: ]
    adj = [[] for _ in range(n + 1)]
    #Prepare adjcent list
    for ind in range(0, len(data) - 1, 2):
        adj[data[ind]].append(data[ind + 1])
        adj[data[ind + 1]].append(data[ind])
    print(bipartite(adj))