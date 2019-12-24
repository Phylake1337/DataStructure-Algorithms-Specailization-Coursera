# Uses python3
from random import randrange

def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, (current + next) % 10
    return sum % 10

def get_fibonacci_sum(n):
    if n <= 1:
        return n
    n = (n%60) + 2
    fibonacci_numbers = [0, 1] + [0] * (n - 1)
    
    for i in range(2, n + 1):
        fibonacci_numbers[i] = (fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]) 

    return (fibonacci_numbers[-1] - 1) % 10 

def fibonacci_partial_sum(from_, to):
    from_, to = from_ % 60, to % 60
    if from_ > to:
        to += 60
    return fibonacci_partial_sum_naive(from_, to)
    


if __name__ == '__main__':
    from_, to = map(int, input().split())
    print(fibonacci_partial_sum(from_, to))
    
#    while True:
#        rand1 = randrange(6000)
#        rand2 = randrange(6000)
#        if fibonacci_partial_sum_naive(rand1, rand1 + rand2) == fibonacci_partial_sum(rand1, rand1 + rand2):
#            print("{} -- {}".format(rand1, rand2), "True")
#        else:
#            print("{} -- {}".format(rand1, rand2), "Something went Wrong!")
#            break