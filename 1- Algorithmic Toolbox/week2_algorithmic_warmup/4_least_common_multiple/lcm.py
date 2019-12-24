# python3
def gcd(a, b):
    if b == 0 :
        return a
    else:
        return gcd(b, a%b)

def lcm(a, b):

    gc = gcd(a, b)
    return a*b // gc


if __name__ == '__main__':
    input_a, input_b = map(int, input().split())
    print(lcm(input_a, input_b))
