#Uses python3
import sys

def lcs2(a, b):
    alen = len(a)
    blen = len(b)
    
    res = [[0 for x in range(alen + 1)] for x in range(blen + 1)]
    
    for i in range (blen + 1):
        for j in range(alen + 1):
            
            if i == 0 or j == 0:
                res[i][j] = 0
            
            elif a[j-1] == b[i-1]:
                res[i][j] = 1 + res[i-1][j-1]
            else:
                res[i][j] = max(res[i-1][j], res[i][j-1])
                
    return res[blen][alen]
                

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
