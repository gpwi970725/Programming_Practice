class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # grid 변수의 공유와 self 사용의 번거로움을 줄이기 위해 중첩함수 사용
        def dfs(i, j):
            if i < 0 or i >= len(grid) or \
               j < 0 or j >= len(grid[0]) or \
               grid[i][j] != "1":
                return
            
            grid[i][j] = "0"
            
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        
        if not grid:
            return 0
        
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    islands += 1
        
        return islands
