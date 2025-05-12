class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque()
        fresh_oranges = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_oranges += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))

        if fresh_oranges == 0:
            return 0

        minutes = 0
        visited = grid
        while queue and fresh_oranges > 0:
            minutes += 1
            for _ in range(len(queue)):
                i, j = queue.popleft()

                for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    new_i = i + dx
                    new_j = j + dy

                    if new_i in range(0, m) and new_j in range(0, n) and visited[new_i][new_j] == 1:
                        visited[new_i][new_j] = 2
                        fresh_oranges -= 1
                        queue.append((new_i, new_j))

        
        return minutes if not fresh_oranges else -1
