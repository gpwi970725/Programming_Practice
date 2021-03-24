from collections import deque


def get_time(now, target):
    next_lists = deque()
    next_lists.append([0, now])
    visited = {now}

    while True:
        now_list = next_lists.popleft()
        for now in now_list[1:]:
            if now == target:
                return now_list[0]

            next_list = [now_list[0] + 1]
            if now >= 1:
                next_list.append(now - 1)
            if now <= 100001:
                next_list.append(now + 1)
            if now <= 50000:
                next_list.append(now * 2)
            next_lists.append(next_list)


N, K = map(int, input().split())
print(get_time(N, K))