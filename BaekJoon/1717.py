"""
# 제너레이터 사용하면 한 줄씩 출력 가능
def get_operations(m):
    for i in range(m):
        operation = map(int, input().split())
        yield operation

def union(a, b):
    a = find(a)
    b = find(b)

    parent[max(a, b)] = min(a, b)

def find(target):
    while target != parent[target]:
        parent[target] = parent[parent[target]]
        target = parent[target]
    return target


n, m = map(int, input().split())
parent = list(range(n+1))

for operation in get_operations(m):
    unionOrFind, a, b = operation

    if unionOrFind == 0:
        union(a, b)
    else:
        print("YES" if find(a) == find(b) else "NO")
"""


# 제출 답안
def union(a, b):
    a = find(a)
    b = find(b)

    parent[max(a, b)] = min(a, b)


def find(target):
    while target != parent[target]:
        parent[target] = parent[parent[target]]
        target = parent[target]
    return target


n, m = map(int, input().split())
parent = list(range(n + 1))

operations = []
for i in range(m):
    operations.append(map(int, input().split()))

for operation in operations:
    unionOrFind, a, b = operation

    if unionOrFind == 0:
        union(a, b)
        print(parent)
    else:
        print("YES" if find(a) == find(b) else "NO")
