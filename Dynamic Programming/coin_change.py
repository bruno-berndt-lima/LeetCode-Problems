class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [10001] * (amount + 1)
        dp[0] = 0

        for i in range(amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(1 + dp[i - coin], dp[i])

        return dp[amount] if dp[amount] != 10001 else -1
