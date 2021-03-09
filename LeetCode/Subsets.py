### my solution
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(index, path):
            if index >= len(nums):
                return
            
            result.append(path)
            for i in range(index+1, len(nums)):
                dfs(i, path + [nums[i]])
              
        result = [[]]
        for i in range(len(nums)):
            dfs(i, [nums[i]])
        
        return result


### book's solution
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(index, path):
            result.append(path)
            for i in range(index, len(nums)):
                dfs(i+1, path + [nums[i]])
              
        result = []
        dfs(0, [])
        
        return result
