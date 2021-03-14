def find(target):
    while target != parent[target]:
        parent[target] = parent[parent[target]]
        target = parent[target]
    return target

def union(a, b):
    a = find(a)
    b = find(b)

    parent[max(a, b)] = parent[min(a, b)]
    

N = int(input())
M = int(input())

if N < 1 or M < 1:
    print("NO")
    quit()

parent = list(range(N))  # 각 도시별로 연결된 도시들 중 가장 작은 수
for target_city in range(N):  # 각 도시별로 연결된 도시들을 입력받는다.
    isLinked = list(map(int, input().split()))
    for compare_city in range(target_city + 1, len(isLinked)):
        if isLinked[compare_city] == 1:
            union(target_city, compare_city)

plan = list(map(int, input().split()))
possible = "YES"
for plan_city in plan:
    if find(plan[0] - 1) != find(plan_city - 1):
        possible = "NO"

print(possible)
        

