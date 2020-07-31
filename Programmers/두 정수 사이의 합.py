def solution(a, b):
    if a > b:
        a, b = b, a
    
    answer_list = list(range(a, b+1))
    answer = sum(answer_list)
    
    return answer