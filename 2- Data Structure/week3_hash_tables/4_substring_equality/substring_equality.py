# python3

def get_hashStr(s, p, x):
    n = len(s)
    hashStr = [0]
    for i in range(1, n + 1):
        res = ((hashStr[-1] * x) % p + ord(s[i - 1]) % p) % p 
        hashStr.append(res)
    return hashStr


def equal(a, b, l, s, x):
    aHashed1 = hashStr1[a+l] % p1 - (pow(x ,l , p1) * hashStr1[a] % p1) % p1
    aHashed2 = hashStr2[a+l] % p2 - (pow(x ,l , p2) * hashStr2[a] % p2) % p2
    bHashed1 = hashStr1[b+l] % p1 - (pow(x ,l , p1) * hashStr1[b] % p1) % p1
    bHashed2 = hashStr2[b+l] % p2 - (pow(x ,l , p2) * hashStr2[b] % p2) % p2
    
    if aHashed1 % p1 == bHashed1 % p1 and aHashed2 % p2 == bHashed2 % p2 :
        return True
    else:
        return False
    
s = input()
q = int(input())
x = 31
p1 = pow(10,9) + 7
p2 = pow(10,9) + 9
hashStr1 = get_hashStr(s, p1, x)
hashStr2 = get_hashStr(s, p2, x)
for i in range(q):
    a, b, l = map(int, input().split())
    print("Yes" if equal(a, b, l, s, x) else "No")
    

