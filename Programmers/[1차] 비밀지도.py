def solution(n, arr1, arr2):
    binArr1 = []
    binArr2 = []
    answer = []
    
    dToB = lambda val, n: format(val, str(n)+'b').replace(' ', '0')
    sToB = lambda val: int(val, 2)
    
    for val1 in arr1:
        binArr1.append(dToB(val1, n))
    for val2 in arr2:
        binArr2.append(format(val2, str(n)+'b').replace(' ', '0'))
    for idx in range(0, n):
        answer.append(dToB(sToB(binArr1[idx])|sToB(binArr2[idx]), n).replace('1', '#').replace('0', ' '))
        
    return answer