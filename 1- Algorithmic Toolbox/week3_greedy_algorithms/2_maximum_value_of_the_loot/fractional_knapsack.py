# Uses python3
import sys 

def get_optimal_value(capacity, weights, values):
    #Calculate absolute value for each item
    valAbs = []
    for i in range(len (values)):
        valAbs.append(values[i] / weights[i])
    
    #Cacluate the final value
    value= 0.0
    while valAbs != []:
        maxAbsInd = valAbs.index(max(valAbs))
        
        currWeight = weights.pop(maxAbsInd)
        currValue = values.pop(maxAbsInd)
        curValAbs = valAbs.pop(maxAbsInd)
        
        
        if capacity > currWeight:
            capacity -= currWeight
            value += currValue
        else:
            value += (capacity * curValAbs)
            capacity = 0
    
    return round(value, 4)

if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))
