def solution(n):
    return ('수박'*int(n/2) if n%2==0 else '수박'*int(n//2)+'수')

n = 3
print(solution(n))


"""
We can solve this problem like this.


method1 >
'''
def solution(n):
    s = "수박" * n
    return s[:n]
'''

method2 >
'''
def water_melon(n):
    return "수박"*(n//2) + "수"*(n%2)
'''
"""
