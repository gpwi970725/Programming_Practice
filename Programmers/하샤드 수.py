def solution(x):
    arr = list(str(x))
    
    total = sum(list(map(int, arr)))
    
    return True if x%total==0 else False
##    return x%total == 0
## 로 해도 같은 결과


x = 12

print(solution(x))
