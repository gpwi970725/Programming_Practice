def solution(arr):
    arr.remove(min(arr))
    
    return arr if arr else [-1]

arr = [4,3,2,1]
print(solution(arr))
