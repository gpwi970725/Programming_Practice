def solution(n):
    arr = [False, False] + ([True] * (n-1))
    
    for (idx, tof) in enumerate(arr):
        if tof:
            false_idx = idx * 2
            while false_idx <= n:
                arr[false_idx] = False
                false_idx += idx
    return len([prime for prime in arr if prime])