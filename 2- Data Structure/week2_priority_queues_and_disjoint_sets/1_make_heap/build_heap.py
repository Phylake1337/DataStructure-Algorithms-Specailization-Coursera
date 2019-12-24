# pyhton3

def parent(i):
    return int(i-1 / 2)
def leftChild(i):
    return 2 * i + 1
def rightChild(i):
    return 2 * i + 2


def SiftDown(i, size, data, pairs):
    maxI = i
    
    l = leftChild(i)
    if l < size and data[l] < data[maxI]:
        maxI = l
        
    r = rightChild(i)
    if r < size and data[r] < data[maxI]:
        maxI = r        
        
    if maxI != i:
        pairs.append((i, maxI))
        data[maxI], data[i] = data[i], data[maxI]
        SiftDown(maxI, size, data, pairs)
        
def get_maxSize(size):
    maxSize = 1
    while size >= maxSize:
        maxSize *= 2
        
    return maxSize - 1  
    

def BuildHeap(data):
    size = len(data)
    maxSize = get_maxSize(size)
    pairs = []
    for i in range(int(maxSize / 2) - 1, -1, -1):
        SiftDown(i, size, data, pairs)
    return pairs 

    
def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = BuildHeap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
