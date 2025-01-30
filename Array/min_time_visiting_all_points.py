class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        min_time = 0

        for i in range(len(points) - 1):
            d_x = abs(points[i+1][0] - points[i][0])
            d_y = abs(points[i+1][1] - points[i][1])

            d = max(d_x, d_y)

            min_time += d

        return min_time
