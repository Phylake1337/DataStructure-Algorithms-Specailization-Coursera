# python3
from collections import deque

def max_sliding_window(sequence, m):
    Qi = deque()
    res = []
    for i in range(len(sequence)):
        if i == 0:
            Qi.appendleft(i)
            if i >= m-1:
                res.append(sequence[Qi[0]])
            continue
        
        if (i - m) >= Qi[0]:
            Qi.popleft()
        
        while Qi:
            if sequence[i] > sequence[Qi[-1]]:
                Qi.pop()
            else:
                break
        Qi.append(i)
        
        if i >= m-1:
            res.append(sequence[Qi[0]])
            
    return res

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())
    print(*max_sliding_window(input_sequence, window_size))

