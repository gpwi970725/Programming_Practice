def solution(n):
    return sum(list(map(int, list(str(n)))))

print(solution(987))

"""
We can use this code.

'''
def solution(n):
    return sum([int(i) for i in str(n)])
'''
"""
