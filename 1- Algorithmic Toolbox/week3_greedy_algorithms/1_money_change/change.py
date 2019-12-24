# Uses python3

def get_change(m):
    coinNum = 0
    while m > 0:
        if m >= 10:
            tens = m // 10
            coinNum += tens
            m -= tens*10
        elif m >= 5:
            m -= 5
            coinNum += 1
        else:
            coinNum += m
            m = 0
    return coinNum

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
