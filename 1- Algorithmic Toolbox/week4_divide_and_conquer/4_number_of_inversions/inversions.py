# Uses python3
import sys

def get_number_of_inversions(a, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, left, ave)
    number_of_inversions += get_number_of_inversions(a, ave, right)
    
    list1 = a[left: ave]
    list2 = a[ave: right]
    j = 0
    b=[]
    while list1 != [] and list2 != []:
        elem1 = list1.pop(0)
        elem2 = list2.pop(0)
        if elem1 <= elem2:
            b.append(elem1)
            list2.insert(0, elem2)
            number_of_inversions += j
        else:
            b.append(elem2)   
            list1.insert(0, elem1) 
            j += 1
            
        if list2 == [] and len(list1) > 1 and j!= 1:
            j += j * (len(list1) - 1)

    if elem1 > elem2:        
        number_of_inversions += j
        
    b = b + list1 + list2
    a[left:right] = b[:] 
    return number_of_inversions

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(get_number_of_inversions(a, 0, len(a)))
