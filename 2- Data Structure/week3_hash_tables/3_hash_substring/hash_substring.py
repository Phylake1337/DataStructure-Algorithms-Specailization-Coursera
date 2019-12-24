# python3
def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def hashFunc(s, p, x):
    res = 0
    for i in range(len(s) - 1, -1, -1):
        res = ((res * x) + ord(s[i])) % p
    return res

def precomputeHash(Text, PatLen, p, x):
    #intialize the output list of hashed substrings
    hashedText = []
    for i in range (len(Text) - PatLen + 1):
        hashedText.append(0)
        
    hashedText[-1] = hashFunc(Text[len(Text) - PatLen: ], p, x)
    
    xPowerp = x ** PatLen
    
    for i in range(len(hashedText) - 2, -1, -1):
        hashedText[i] = ((x * hashedText[i+1]) + (ord(Text[i]) - (ord(Text[i + PatLen]) * xPowerp))) % p
    return hashedText

def get_occurrences(pattern, text):
    p = 100000000007
    x = 1
    pHash = hashFunc(pattern, p, x)
    tHash = precomputeHash(text, len(pattern), p, x)
    result = []
    for i in range(len(tHash)):
        
        if tHash[i] == pHash and text[i : i + len(pattern)] == pattern:
            result.append(i)
            
    return result

  
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

