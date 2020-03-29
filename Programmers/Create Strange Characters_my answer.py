def solution(s):
    strange_str = []
    idx = 0
    for alphabet in list(s):
        if alphabet is ' ':
            idx = 0
            strange_str.append(' ')
            continue
        else:
            strange_str.append(alphabet.upper()) if idx%2==0 else strange_str.append(alphabet.lower())
            idx = idx + 1
        
    
    return ''.join(strange_str)

s = "try hello worlD"
print(solution(s))




"""
We can also solve like this.


method1 >
'''
def solution(s):
    return ' '.join([''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(w)]) for w in s.split()])
'''

method2 >
'''
def solution(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))
'''
"""
