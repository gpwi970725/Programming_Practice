def solution(s):
    index = len(s)//2
    return (s[index] if len(s)%2 != 0 else s[index-1:index+1])