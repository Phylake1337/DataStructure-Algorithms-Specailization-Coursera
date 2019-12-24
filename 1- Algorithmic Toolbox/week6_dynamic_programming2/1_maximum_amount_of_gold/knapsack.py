# Uses python3
import sys

def optimal_weight(W, w):
    wlen = len(w)
    result = list([0 for _ in range(W + 1)] for _ in range(wlen + 1))
    for i in range(1, wlen + 1) :
        for j in range(1, W + 1):
            result[i][j] = result[i-1][j]
    
            if w[i - 1] <= j:
                result[i][j] = max(result[i - 1 ][j - w[i-1]] + w[i - 1] ,result[i][j])
    return result[-1][-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
