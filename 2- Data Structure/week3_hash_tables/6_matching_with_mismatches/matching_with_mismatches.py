# python3
import sys

#get all hashed prefixes of an s string
def get_hashStr(s, p, x):
    n = len(s)
    hashStr = [0]
    for i in range(1, n + 1):
        res = ((hashStr[-1] * x) % p + ord(s[i - 1]) % p) % p 
        hashStr.append(res)
    return hashStr

#Hash a string using the hashed prefixes
def Hash(hashStr, a, l, p, x):
    return hashStr[a+l] % p - (pow(x ,l , p) * hashStr[a] % p) % p

#get how many differences recursivly
def get_Diff(tHashStr, pHashStr, s1, s2, l, p, x):
    
    textHashed = Hash(tHashStr, s1, l, p, x)
    patternHashed = Hash(pHashStr, s2, l, p, x)
    
    if not(textHashed == patternHashed):
        if l == 1:
            return 1
        else:
            return ( get_Diff(tHashStr, pHashStr, s1, s2, l//2, p, x) 
                    + get_Diff(tHashStr, pHashStr, s1+l // 2, s2+l // 2, l - l//2, p, x))
    else:
        return 0
    
    
def solve(k, text, pattern):
    textHashStr = get_hashStr(text, p, x)
    patternHashStr = get_hashStr(pattern, p, x)
    tLen, pLen = len(text), len(pattern)
    result = []
    for i in range(tLen - pLen + 1):
        Diff_num = get_Diff(textHashStr, patternHashStr, i, 0, pLen, p , x)
        if Diff_num <= k:
            result.append(i)
    return result

p = pow(10, 9) + 9
x = 31
for line in sys.stdin.readlines():
	k, t, p = line.split()
	ans = solve(int(k), t, p)
	print(len(ans), *ans)
