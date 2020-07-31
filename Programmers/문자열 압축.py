def solution(s):
    sLen = len(s)
    answer = sLen
    ansStr = ""
    
    for unitNum in range(1, (int(sLen/2)+1 if sLen%2 == 1 else int(sLen/2)+1)):
        repNum = 1
        idx = 0
        repStr = s[:unitNum]
        ansStr = ""

        print("repStr: '" + repStr + "'")
        
        while idx < sLen-unitNum:

            print(str(unitNum) + " ansStr: '" + ansStr + "' compare: '" + s[idx:idx+unitNum] + "' and '" + s[idx+unitNum:idx+(2*unitNum)] + "'")
            
            if s[idx:idx+unitNum] == s[idx+unitNum:idx+(2*unitNum)]:
                repStr = s[idx:idx+unitNum]
                repNum = repNum + 1
            else:
                ansStr = ansStr + (("" if repNum == 1 else str(repNum)) + s[idx:idx+unitNum])
                repNum = 1
            idx = idx + unitNum
        ansStr = ansStr + ("" if repNum == 1 else str(repNum)) + s[idx:]

        print(str(unitNum) + "     " + ansStr)
        
        if answer > len(ansStr):
            answer = len(ansStr)
        
        
    print(ansStr)
    return answer



s = "ababcdcdababcdcd"
print(solution(s))

