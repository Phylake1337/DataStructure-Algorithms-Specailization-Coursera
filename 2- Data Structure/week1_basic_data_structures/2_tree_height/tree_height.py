# python3

import sys 
import threading

def formTree(n, parents):
    tree = []
    for i in range(n):
        tree += [[]]
    
    for i in range(len(parents)):
        if parents[i] == -1:
            continue
        
        tree[parents[i]].append(i)

    return tree

def compute_height(head, tree):
    if tree[head] == []:
        return 1 
    else:
        maxH = 0
        for node in tree[head]:
            maxH = max(compute_height(node, tree), maxH)
            
        return maxH + 1


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    tree = formTree(n, parents)
    print(compute_height(parents.index(-1), tree))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
