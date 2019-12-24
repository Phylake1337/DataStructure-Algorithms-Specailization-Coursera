# python3

import sys
from collections import namedtuple

Answer = namedtuple('answer_type', 'i j len')

def solve(s, t):
	ans = Answer(0, 0, 0)
	for i in range(len(s)):
		for j in range(len(t)):
			for l in range(min(len(s) - i, len(t) - j) + 1):
				if (l > ans.len) and (s[i:i+l] == t[j:j+l]):
					ans = Answer(i, j, l)
	return ans

def get_hashStr(s, p, x):
    n = len(s)
    hashStr = [0]
    for i in range(1, n + 1):
        res = ((hashStr[-1] * x) % p + ord(s[i - 1]) % p) % p 
        hashStr.append(res)
    return hashStr

def Solve(s, t):
    p ,x = pow(10,9) + 7, 31
    sHashedStr = get_hashStr(s, p, x)
    tHashedStr = get_hashStr(t, p, x)
    


for line in sys.stdin.readlines():
    s, t = line.split()
    ans = solve(s, t)	
    print(ans.i, ans.j, ans.len)	
