import sys

def find(target):
    while target != connected[target]:
        connected[target] = connected[connected[target]]
        target = connected[target]
    return target

def union(a, b):
    a = find(a)
    b = find(b)

    connected[b] = a


N = int(input())  # 컴퓨터의 수
M = int(input())  # 연결할 수 있는 선의 수

connect = {}
for i in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    if a != b:
        key = (min(a, b), max(a, b))
        if key in connect:
            connect[key] = min(c, connect[key])
        else:
            connect[key] = c

# 비용이 작은 순서대로 담긴 연결 정보
sorted_connect = sorted(connect, key=lambda x: connect[x])

# 각 컴퓨터마다 연결된 컴퓨터들 중 가장 작은 번호 리스트
connected = list(range(N + 1))

price = 0
for a, b in sorted_connect:
    # 모든 컴퓨터를 연결할 수 없는 경우는 없으므로 반드시 조건문 탐
    if len(set(connected[1:])) == 1:
        break

    if find(a) != find(b):
        union(a, b)
        price += connect[(a, b)]
        connected = list(map(lambda x: find(x) if x == connected[b] else x, connected))


print(price)
