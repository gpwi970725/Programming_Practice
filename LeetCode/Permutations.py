### solution 1
from copy import deepcopy

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(array, remaining):  # array: 현재 만드는중인 결과 배열 / remaining: array에 붙여야 할 값 배열
            if not remaining:
                answer.append(array)
                return
            
            for num in remaining:
                next_remaining = deepcopy(remaining)
                next_remaining.remove(num)
                dfs(array + [num], next_remaining)
        
        answer = []
        dfs([], nums)
        
        return answer


### solution 2
import itertools

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 구현의 효율성, 성능을 위해 itertools 라이브러리 사용
        return itertools.permutations(nums)
