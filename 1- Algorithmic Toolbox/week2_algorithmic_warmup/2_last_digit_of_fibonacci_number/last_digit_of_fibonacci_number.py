# python3
def last_digit_of_fibonacci_number(n):
    assert 0 <= n <= 10 ** 7
    fibSeries = [0, 1] + [None] * (n-1)
    for i in range(2, n+1):
        fibSeries[i] = (fibSeries[i-1] + fibSeries[i-2]) % 10
    return fibSeries[n] % 10


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_fibonacci_number(input_n))
