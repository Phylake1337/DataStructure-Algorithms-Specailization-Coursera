# python3

def max_pairwise_product(numbers):
    
    fst_n = max(numbers)
    numbers.remove(fst_n)
    scd_n = max(numbers)
    return fst_n * scd_n


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
