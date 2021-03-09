### solution 1
from copy import deepcopy

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(array, next_elements):  # array: 현재 만드는중인 배열 / next_elements: array에 붙일 수 있는 요소 목록
            if len(array) == k:
                answer.append(array)
                return
            
            remaining = deepcopy(next_elements)
            for next_element in next_elements:
                remaining.remove(next_element)
                dfs(array + [next_element], remaining)
            
        answer = []
        dfs([], [_ for _ in range(1, n+1)])
        
        return answer

### solution 2
import itertools

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return itertools.combinations(range(1, n + 1), k)
