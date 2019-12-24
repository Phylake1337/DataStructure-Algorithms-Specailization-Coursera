# Uses python3
import sys

def get_change(m):
    if m > 4:
        results = [0] * m
        results[0] = results[2] =results[3] = 1 
        results[1] = 2
    else:
        results = [1,2,1,1]

    for i in range(4, m):
        results[i] = min(results[i-1], results[i-3], results[i-4]) + 1
            
    return results[m-1]
if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
