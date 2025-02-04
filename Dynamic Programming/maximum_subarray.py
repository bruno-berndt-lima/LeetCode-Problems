class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = nums
        max_sum = dp[0]
      
        for i in range(1, len(nums)):
            dp[i] = max(dp[i], dp[i - 1] + dp[i])

            if dp[i] > max_sum:
                max_sum = dp[i]

        return max_sum
