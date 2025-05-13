class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        final_sum = 0
        
        # Binomial coefficient
        coefficient = 1

        for i in range(n):
            final_sum = (final_sum + coefficient * nums[i]) % 10

            if i < n - 1:
                coefficient = coefficient * (n - 1 - i) // (i + 1)

        return final_sum
