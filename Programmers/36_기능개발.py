def solution(progresses, speeds):
    answer = []
    num = 1


    date = (100-progresses[0])/speeds[0]
    criterion = date
    
    for i in range(1, len(speeds)):
        date = (100-progresses[i])/speeds[i]

        if date<=criterion:
            num += 1
        else:
            answer.append(num)
            num = 1

    answer.append(num)
        
    return answer


progresses = [93,30,55]
speeds = [1,30,5]

print(solution(progresses, speeds))
