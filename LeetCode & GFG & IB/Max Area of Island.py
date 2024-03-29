from typing import List

class Solution:
    
    def dfs (self, grid, r,c):
        grid[r][c] = 0
        num = 1
        lst = [(r+1,c), (r-1, c), (r,c+1), (r,c-1)]
        # print (lst)
        
        for row, col in lst:
            if row >=0 and col >= 0 and row <len(grid) and col <len(grid[0]) and grid[row][col] == 1:
                num += self.dfs(grid, row, col)
        return num
    
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area_islands = 0
        sum = 0
        for r in range (len(grid)):
            for c in range (len(grid[0])):
                if grid [r][c] == 1:
                    sum = max(sum,self.dfs (grid,r,c)    )
        return sum

ob = Solution()
num = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
print (ob.maxAreaOfIsland(num))