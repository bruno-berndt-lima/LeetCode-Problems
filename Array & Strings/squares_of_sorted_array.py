class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        sorted_nums = [0] * len(nums)

        i = len(nums) - 1
        while i >= 0:
            if abs(nums[left]) < abs(nums[right]):
                sorted_nums[i] = nums[right] * nums[right]
                right -= 1
            elif abs(nums[left]) >= abs(nums[right]):
                sorted_nums[i] = nums[left] * nums[left]
                left += 1
            i -= 1

        return sorted_nums
