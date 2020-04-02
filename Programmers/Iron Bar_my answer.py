from collections import deque

def solution(arrangement):
    arrangement = arrangement.replace("()", "|")
    arr_queue = deque(arrangement)
    iron_bar = []
    piece = 0
    
    while arr_queue:
        now = arr_queue.popleft()
        if now == '|':
            piece += len(iron_bar)
        elif now == '(':
            iron_bar.append(now)
            piece += 1
        else:
            iron_bar.pop()
    
    return piece


arrangement = "()(((()())(())()))(())"
print(solution(arrangement))


"""
We can solve like this.

'''
def solution(arrangement):
    answer = 0
    sticks = 0
    rasor_to_zero = arrangement.replace('()','0')

    for i in rasor_to_zero:
        if i == '(':
            sticks += 1
        elif i =='0' :
            answer += sticks
        else :
            sticks -= 1
            answer += 1

    return answer
'''
"""
