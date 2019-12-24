#Uses python3
import sys
       
def get_max(a):
    '''
    Extract the maxmium number in a list i a special way, 3 > 21 and 3 < 31 as problem require
    '''
    maxNum = 0
    for num in a:
        #if both numbers are same size then return the max
        if len(str(num)) == len(str(maxNum)):
            maxNum = max(num, maxNum)
        #if not, should be treated in a special way
        else:
            #get left most digits of the maximum number with same size as other number
            #and campare it with the minimum one
            lenDiff = abs(len(str(num)) - len(str(maxNum)))
            LMDigits = max(num, maxNum) // (10 ** lenDiff) 
            
            if LMDigits > min(num, maxNum):
                maxNum = max(num, maxNum)
            elif LMDigits < min(num, maxNum):
                maxNum = min(num, maxNum)
            else:
                #if LMDdigits and minimum number are equal, then we should compare minimum 
                #number with a shifted version of LMDigits >>
                Max = str(max(maxNum, num))
                Min = str(min(maxNum, num)) 
                
                for i in range (len(Max) - len(str(Min)) + 1):
                    if int(Min) == int(Max[i: i+len(Min)]):
                        continue
                    elif int(Min) > int(Max[i: i+len(Min)]):
                        maxNum = int(Min)
                    else:
                        maxNum = int(Max)        
    return maxNum

def largest_number(a):
    res = ""
    while a != []:
        maxElem = get_max(a)
        res += str(maxElem)
#        print("{} --  {}".format(maxElem, a))         
        a.remove(maxElem)
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    a = data[1:]
    print(largest_number(a))
    
