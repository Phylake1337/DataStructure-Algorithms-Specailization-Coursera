# Uses python3
import sys
import random

def partition3(a, l, r):
    x = a[l]
    j = l
    shft = 0
    for i in range(l + 1, r + 1):
        if a[i] == x:
            a.insert(l, a.pop(i))
            shft += 1
            j += 1
            continue
        if a[i] < x:
            j += 1
            a[i], a[j] = a[j], a[i]

    for i in range(l, (l + shft+1)):
            a[i], a[l + j - i] = a[l + j - i], a[i]
            

    return (j - shft, j)

def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m1, m2 = partition3(a, l, r)
#    print("Current a : ", a[l:r+1])
#    print("m1 : {}, a[m1] : {}".format(m1, a[m1]))
#    print("m2 : {}, a[m2] : {}".format(m2, a[m2]))
#    print("Sub1 : ", a[l : m1 - 1 + 1])
#    print("Sub2 : ", a[m2 + 1 : r + 1])
#    print("=========================================")
    randomized_quick_sort(a, l, m1 - 1);
    randomized_quick_sort(a, m2 + 1, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
