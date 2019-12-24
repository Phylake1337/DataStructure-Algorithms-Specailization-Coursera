def rope(Str, i, j, k):
    subStr = Str[i : j + 1]
    Str = "{}{}".format(Str[ : i], Str[j + 1 : ])
    return "{}{}{}".format(Str[:k], subStr, Str[k:])

Str = input()
n = int(input())
for _ in range (n):
    i, j, k = map(int, input().strip().split())
    Str = rope(Str, i, j ,k)
print(Str)