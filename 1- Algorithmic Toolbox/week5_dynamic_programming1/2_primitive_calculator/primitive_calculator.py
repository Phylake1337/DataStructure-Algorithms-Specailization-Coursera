# Uses python3
import sys


def update_seq(seqList):     
    lenList = []
    for slist in seqList:
        if slist == float("inf"):
            lenList.append(slist)
        else:
            lenList.append(len(slist))
            
    if lenList[0] == min(lenList[0], lenList[1], lenList[2]):
        return seqList[0] + [seqList[0][-1] * 3]
    
    elif lenList[1] == min(lenList[0], lenList[1], lenList[2]):            
        return seqList[1] + [seqList[1][-1] * 2]
    
    else:
        return seqList[2] + [seqList[2][-1] + 1]
    
        
        
def Optimal_seq_DP(n):
    if n > 3: 
        results = [[0]] * (n + 1)
        results[2] = [1, 2]
        results[3] = [1, 3]
    else:
        results = [[0],[1],[1,2],[1,3]]
    
    
    for i in range(4, n + 1):
        if (i % 3 == 0) and (i % 2 == 0):
            results[i] = update_seq([results[i // 3],
                                                   results[i // 2],
                                                   results[i - 1]])
                        
        elif (i % 3 != 0) and (i % 2 == 0):
            results[i] = update_seq([float("inf"),
                                                   results[i // 2],
                                                   results[i - 1] ])
            
        elif (i % 3 == 0) and (i % 2 != 0):
            results[i] = update_seq([results[i // 3],
                                                   float("inf"),
                                                   results[i - 1]])
            
        else:
            results[i] = update_seq([float("inf"),
                                                   float("inf"),
                                                   results[i - 1]])            
            
    return results[n]


input = sys.stdin.read()
n = int(input)
sequence = list(Optimal_seq_DP(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
