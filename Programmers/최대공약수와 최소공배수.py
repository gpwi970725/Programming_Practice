# 유클리드 호제법으로 최대공약수 구하는 함수
def gcd(a, b):
    if a < b:
        a, b = b, a
    
    while b:
        a, b = b, a%b
    
    return a

def solution(n, m):
    answer = []
    
    answer.append(gcd(n, m))
    answer.append(int(n*m/answer[0]))
    
    return answer


n = 3
m = 12

print(solution(n, m))
