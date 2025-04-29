class Solution:
    # Values that will make the full path of the recursion for a given island.
    # Islands with the same path are equal.
    # X: Start
    # O: Out of bounds OR water
    # U: Up
    # D: Down
    # R: Right
    # L: Left
    
    def compute_path(self, grid, i, j, m, n, direction):
        if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0:
            return direction + "O"
        
        grid[i][j] = 0
        
        left = self.compute_path(grid, i, j - 1, m, n, "L")
        right = self.compute_path(grid, i, j + 1, m, n, "R")
        up = self.compute_path(grid, i - 1, j, m, n, "U")
        down = self.compute_path(grid, i + 1, j, m, n, "D")
        
        return direction + left + right + up + down
 
    
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        if grid is None or len(grid) == 0:
            return 0
        
        distinct_islands = set()
        m, n  = len(grid), len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    path = self.compute_path(grid, i, j, m, n, "X")
                    distinct_islands.add(path)
                    
        return len(distinct_islands)
