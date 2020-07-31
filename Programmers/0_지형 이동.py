from collections import deque
import numpy as np

def solution(land, height):
    land_dict = dict(enumerate(np.ravel(land)))
    
    need_visit, visited = deque(), deque()
    n = len(land)

    need_visit.append(0)

    while need_visit:
        node = need_visit.pop()
        
        if node not in visited:
            visited.append(node)
            
            next_nodes = list(filter(lambda x: x>=0 and x<n*n
                                     and abs(land_dict[x]-land_dict[node])<=height,
                              [node-1,node+1,node-n,node+n]))
            need_visit.extend(next_nodes)

    return visited



land = [[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]]
height = 1

print(solution(land, height))
