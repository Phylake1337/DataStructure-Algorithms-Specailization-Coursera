# python3
def perLen(n, m):
    previous, current = 0, 1
    count = 0
    while True:
        previous, current = current, (previous + current) % m
        count += 1
        if previous == 0 and current == 1:
            return count

def fibonacci_number_again_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3
    len = perLen(n, m)
    #Here's the trick, after getting the priod length, divide the whole n by len to get the new small n
    n = n % len
    return fibonacci_number_again_naive(n, m)


if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_n, input_m))
