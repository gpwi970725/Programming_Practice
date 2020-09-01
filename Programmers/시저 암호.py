def solution(s, n):
    answer = []
    s_list = list(s)
    
    for alphabet in s_list:
        ascCode = ord(alphabet)
        if ascCode >= 97:
            ascCode += n
            if ascCode > 122:
                ascCode = 96 + (ascCode-122)
        elif ascCode >= 65:
            ascCode += n
            if ascCode > 90:
                ascCode = 64 + (ascCode-90)
                
        answer.append(chr(ascCode))
    
    answer = ''.join(answer)
    
    return answer

s = "a B z"
n = 4
print(solution(s, n))
