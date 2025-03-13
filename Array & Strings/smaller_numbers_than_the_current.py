class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []

        nums_copy = sorted(nums)

        counts = {}
        for i, num in enumerate(nums_copy):
            if num not in counts:
                counts[num] = i

        for num in nums:
            res.append(counts[num])

        return res
                
