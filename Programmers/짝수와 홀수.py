def solution(num):
    return "Even" if num%2==0 else "Odd"

num = 3
print(solution(num))



'''
<cf solution>

def solution(num):
    return ["Even", "Odd"][num & 1]
'''
