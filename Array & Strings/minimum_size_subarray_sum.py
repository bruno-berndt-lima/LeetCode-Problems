class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float('inf')
        current_sum = 0
        l = 0

        for r in range(len(nums)):
            current_sum += nums[r]

            if current_sum >= target:
                while current_sum >= target:
                    min_length = min(min_length, r - l  + 1)
                    current_sum -= nums[l]
                    l += 1

        return min_length if min_length != float('inf') else 0
