def solution(arr, divisor):
    answer = []
    for x in arr:
        if x%divisor == 0:
            answer.append(x)
    
    return ([-1] if len(answer)==0 else sorted(answer))