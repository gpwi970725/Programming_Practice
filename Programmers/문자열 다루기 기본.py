def solution(s):
    try:
        int(s)
    except:
        return False
    if len(s)!=4 and len(s)!=6:
        return False
    else:
        return True


print(solution("1234"))

'''
We can change like this answer.

"""
return s.isdigit() and len(s) in (4, 6)
"""
'''
