class Solution:
    def climbStairs(self, n: int) -> int:
        # n = 0 -> 0
        # n = 1 -> 1
        # n = 2 -> 2 (1, 1) (2)
        # n = 3 -> 3 (1, 1, 1) (1, 2) (2, 1)
        # n = 4 -> 5 (1, 1, 1, 1) (1, 2, 1) (1, 1, 2) (2, 1, 1) (2, 2)

        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        
        if n >= 2:
            dp[2] = 2

            for i in range(3, n + 1):
                dp[i] = dp[i - 1] + dp[i - 2]


        return dp[n]
