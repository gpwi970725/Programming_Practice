def solution(n):
    arr = list(str(n))
    arr.reverse()
    
    return list(map(int, arr))

print(solution(12345))


"""
We can minimize like this code

'''
def solution(n):
    return list(map(int, reversed(str(n))))
'''
"""
