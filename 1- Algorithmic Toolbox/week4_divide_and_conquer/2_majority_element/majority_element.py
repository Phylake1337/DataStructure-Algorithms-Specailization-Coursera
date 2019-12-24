# Uses python3
def majority_element_naive(elements):
    assert len(elements) <= 10 ** 5
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1
    return 0

def majority_element(elements):
    assert len(elements) <= 10 ** 5
    n = len(elements)
    cnt = {}
    for num in elements:
        try:
            cnt[num] += 1
        except:
            cnt[num] = 1
    for k,v in cnt.items():
        if v > n/2:
            return 1
    return 0

majority_element([2,3,9,2,2])



if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))
    
#    while True:
#        Input =[]
#        for i in range(10000):
#            Input.append(randint(0,10**9))
#        if majority_element(Input) == majority_element_naive(Input):
#            print("True!")
#        else:
#            print(Input)
#            print(majority_element(Input),majority_element_naive(Input))
#            break
            
