def solution(stones, k):
    cnt = max(stones)

    for i in range(len(stones)-k+1):
        temp = max(stones[i:i+k])
        
        print(cnt, temp)
        if cnt > temp:
            cnt = temp

        print(cnt, min(stones[i+1:]))
        if cnt <= min(stones[i+1:]):
            break

        print()

    return cnt


stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3

print(solution(stones, k))
