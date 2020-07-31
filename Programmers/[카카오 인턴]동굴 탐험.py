from collections import deque

def solution(n, path, order):
    path.sort()
    tree = [[] for _ in range(n)]
    for a, b in path:
        tree[a].append(b)
        tree[b].append(a)
    
    must_go = []        # 선방문 목록
    cant_go = []        # 방문불가능 목록
    cant_go_idx = []    # 방문불가능 목록 인덱스
    for idx, val in enumerate(order):
        cant_go_idx.append(idx)
        must_go.append(val[0])
        cant_go.append(val[1])
        
    visit = deque([0])
    visited = deque()
    while visit:
        now = visit.popleft()
        
        # now가 방문불가능 목록에 있으면
        cnt = 0
        while now in cant_go:
            visit.append(now)
            
            if cnt == len(visit):
                return False
            
            now = visit.popleft()
            cnt += 1
        
        # 방문한 방 목록에 now 추가
        visited.append(now)
        
        # 방문할 방 목록에 방문하지 않은 방 추가
        for x in tree[now]:
            if x not in visited:
                visit.append(x)
                
        # now가 선방문 목록에 있으면
        if now in must_go:
            delIdx = cant_go_idx.index(must_go.index(now))
            del cant_go_idx[delIdx]
            del cant_go[delIdx]
    
    return True


n = 9
path = [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]]
order = [[8,5],[6,7],[4,1]]

print(solution(n, path, order))
