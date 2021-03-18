from heapq import *
import sys


def kruskal(house_count, road_map):
    def find(target):
        while target != parents[target]:
            parents[target] = parents[parents[target]]
            target = parents[target]
        return target

    def union(target1, target2):
        target1 = find(target1)
        target2 = find(target2)
        target1, target2 = min(target1, target2), max(target1, target2)
        parents[target2] = target1

    parents = list(range(house_count + 1))
    cost_min = 0
    visit_count = house_count - 2
    while visit_count:
        cost, house1, house2 = heappop(road_map)
        if find(house1) != find(house2):
            union(house1, house2)
            cost_min += cost
            visit_count -= 1

    return cost_min


house_count, road_count = map(int, input().split())
road_map = []
for i in range(road_count):
    house1, house2, cost = map(int, sys.stdin.readline().split())
    heappush(road_map, (cost, house1, house2))

print(kruskal(house_count, road_map))
