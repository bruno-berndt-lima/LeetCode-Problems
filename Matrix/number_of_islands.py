class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row, col):
            if row < 0 or col < 0 or row >= m or col >= n or grid[row][col] == '0':
                return

            grid[row][col] = '0'

            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

            for dr, dc in directions:
                dfs(row + dr, col + dc)

        m, n = len(grid), len(grid[0])
        n_islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    n_islands += 1

        return n_islands
