class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()

        for i, num in enumerate(nums):
            if num != i:
                return num - 1      

            if i == n - 1:
                return num + 1      

        return 0

        
