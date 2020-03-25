def solution(N, stages):
    failNum = []
    failRate = []
    answer = []
    restUserNum = len(stages)
    
    for i in range(0, N):
        failNum.append(stages.count(i+1))
    
    for i in range(0, N):
        failRate.append(failNum[i]/restUserNum)
        restUserNum = restUserNum - failNum[i]

    sortList = sorted(failRate, reverse=True)

    for i in range(0, N):
        idx = failRate.index(sortList[i])
        answer.append(idx+1)
        failRate[idx] = -1
    
    return answer


N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

print(solution(N, stages))
