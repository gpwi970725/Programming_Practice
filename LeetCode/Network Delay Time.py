from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # graph : {출발노드 : (시간, 도착노드), ...}
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((w, v))
        
        # queue : [(출발지부터 노드까지의 시간, 노드), ...]
        queue = []
        # result : {노드: 출발지부터 노드까지의 시간, ...}
        result = {}
        heapq.heappush(queue, (0, k))
        while queue:
            now_time, now_node = heapq.heappop(queue)
            if now_node not in result:
                result[now_node] = now_time
                for time, node in graph[now_node]:
                    heapq.heappush(queue, (now_time + time, node))
        
        if len(result) == n:
            return max(result.values())
        return -1