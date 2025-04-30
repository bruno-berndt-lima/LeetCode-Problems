class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(row, col, m, n, grid):
            if row < 0 or col < 0 or row >= m or col >= n or grid[row][col] == 0:
                return 0

            grid[row][col] = 0
            area = 1

            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc

                area += dfs(new_row, new_col, m, n, grid)
            
            return area

        max_area = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = dfs(i, j, m, n, grid)
                    max_area = max(max_area, area)

        return max_area
