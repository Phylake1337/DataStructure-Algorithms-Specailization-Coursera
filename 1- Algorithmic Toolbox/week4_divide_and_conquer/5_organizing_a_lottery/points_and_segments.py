# Uses python3
import sys

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    line = []
    for i in starts:
        line.append((i, 'l'))

    for i in ends:
        line.append((i, 'r'))

    for i in range(len(points)):
        line.append((points[i], 'p', i))
    
    line = sorted(line)
    segNum = 0
    for tpl in line:
        if tpl[1] == 'l':
            segNum += 1
        elif tpl [1] == 'r':
            segNum -= 1
        else:
            cnt[tpl[2]] = segNum
            
    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
