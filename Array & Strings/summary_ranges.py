class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        i = 0

        while i < len(nums):
            start = nums[i]
            
            while i + 1 < len(nums) and nums[i + 1] == nums[i] + 1:
                i += 1

            end = nums[i]
            ranges.append(f"{start}->{end}" if start != end else f"{start}")
            i += 1

        return ranges
