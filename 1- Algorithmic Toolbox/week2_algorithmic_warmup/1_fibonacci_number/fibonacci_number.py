# python3

def fibonacci_number(n):
    assert 0 <= n <= 45
    fibSeries = [0, 1] + [None] * (n-1)
    for i in range(2, n+1):
        fibSeries[i] = fibSeries[i-1] + fibSeries[i-2]
    return fibSeries[n]

if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
