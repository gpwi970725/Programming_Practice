from collections import defaultdict
from heapq import *
import sys


def prim(first_node, edges):
    mst = []
    # 해당 노드에 해당 간선을 추가
    adjacent_edges = defaultdict(list)
    for weight, node1, node2 in edges:
        adjacent_edges[node1].append((weight, node1, node2))
        adjacent_edges[node2].append((weight, node2, node1))

    # 처음 선택한 노드를 연결된 노드 집합에 삽입
    connected_nodes = {first_node}
    # 선택된 노드에 연결된 간선을 간선 리스트에 삽입
    candidate_edges = adjacent_edges[first_node]
    # 오름 차순으로 정렬
    heapify(candidate_edges)

    while candidate_edges:
        weight, node1, node2 = heappop(candidate_edges)
        # 사이클 있는지 확인 후 연결
        if node2 not in connected_nodes:
            connected_nodes.add(node2)
            mst.append((weight, node1, node2))

            for edge in adjacent_edges[node2]:
                if edge[2] not in connected_nodes:
                    heappush(candidate_edges, edge)

    return mst


def my_prim(first_node, graph_tuple):
    graph = defaultdict(list)
    for weight, node1, node2 in graph_tuple:
        graph[node1].append((weight, node2))  # 비용, 인접 노드
        graph[node2].append((weight, node1))

    tree = {first_node}  # 현재 만들어진 트리
    edges = graph[1]  # 방문할 간선 리스트 (최소 힙)
    total_price = 0  # 최소 스패닝 트리의 가중치
    heapify(edges)
    while edges:  # 방문할 간선이 있는동안 반복
        weight, node = heappop(edges)
        if node not in tree:  # 가려는 노드가 현재 트리에 없는지 확인
            tree.add(node)
            total_price += weight

            # 방문할 간선 리스트에는 이미 방문한 노드 포함하지 않음
            for edge in graph[node]:
                if edge[1] not in tree:
                    heappush(edges, edge)

    return total_price


def my_kruskal(node_count, graph_tuple):
    def find(target):
        while target != parent_node[target]:
            parent_node[target] = parent_node[parent_node[target]]
            target = parent_node[target]

        return target

    def union(target1, target2):
        target1 = find(target1)
        target2 = find(target2)
        target1, target2 = max(target1, target2), min(target1, target2)

        parent_node[target1] = target2

    heapify(graph_tuple)
    parent_node = list(range(node_count + 1))
    total_weight = 0
    visit_count = node_count - 1
    while visit_count:
        weight, node1, node2 = heappop(graph_tuple)
        if find(node1) != find(node2):
            union(node1, node2)
            total_weight += weight
            visit_count -= 1

    return total_weight


V, E = map(int, input().split())  # 노드 수, 간선 수
graph = []
for i in range(E):
    A, B, C = map(int, sys.stdin.readline().split())
    graph.append((C, A, B))

# print(my_prim(1, graph))
print(my_kruskal(V, graph))
