def solution(N, stages):
    # user_in_step : stage에 도전 중인(클리어하지 못한) 사용자 수
    user_in_step = [0] * (N + 1)
    
    # complete : 마지막 stage까지 클리어 한 사용자 수
    complete = 0
    for stage in stages:
        if stage == N + 1:
            complete += 1
            continue
        user_in_step[stage] += 1
    
    # divisor : 실패율을 구하기 위해 나누는 수(스테이지에 도달한 사용자 수)
    divisor = complete
    for i in range(N, 1 - 1, -1):
        divisor += user_in_step[i]
        if divisor != 0:
            user_in_step[i] /= divisor
        
    # user_in_step의 인덱스는 0~N으로 이루어져있기 때문에 인덱스 0 삭제
    del user_in_step[0]
    
    stages = [_ for _ in range(1, N+1)]
    answer = list(zip(user_in_step, stages))
    answer = sorted(answer, key = lambda x: (-x[0], x[1]))    
    
    return list(zip(*answer))[1]
