class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(index, path, path_sum):
            if path_sum > target:
                return
            if path_sum == target:
                result.append(path)
                return
            
            for i in range(index, len(candidates)):
                dfs(i, path + [candidates[i]], path_sum + candidates[i])
            
                
        result = []
        candidates = list(filter(lambda x: x != 0, candidates))
        dfs(0, [], 0)
        
        return result
