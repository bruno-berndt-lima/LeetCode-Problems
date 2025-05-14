class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        non_increasing = [0 for _ in range(n)]
        non_decreasing = [0 for _ in range(n)]

        for i in range(1, n):
            if security[i] <= security[i - 1]:
                non_increasing[i] = non_increasing[i - 1] + 1
            else:
                non_increasing[i] = 0

        for i in range(n - 2, -1, -1):
            if security[i] <= security[i + 1]:
                non_decreasing[i] = non_decreasing[i + 1] + 1
            else:
                non_decreasing[i] = 0

        result = []
        for i in range(n):
            if non_increasing[i] >= time and non_decreasing[i] >= time:
                result.append(i)

        return result
