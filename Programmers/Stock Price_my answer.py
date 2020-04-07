"""
1st and 2nd answers didn't pass the efficiency test.



My 1st answer>

'''
def solution(prices):
    answer = []

    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] > prices[j]:
                if j == i+1:
                    how_long += 1
                break
            else:
                how_long += 1
                
        answer.append(how_long)
    
    return answer
'''



My 2nd answer>

'''
def solution(prices):
    answer = []

    length = len(prices)
    
    for i in range(0, length-1):
        try:
            value = list(filter(lambda x: prices[i]>x, prices[i+1:length]))[0]
            answer.append(prices.index(value, i+1)-i)
        except:
            answer.append(length-i-1)
    answer.append(0)
    
    return answer
'''


final pass answer>
"""
def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer

prices = [1, 2, 3, 2, 3]
print(solution(prices))
