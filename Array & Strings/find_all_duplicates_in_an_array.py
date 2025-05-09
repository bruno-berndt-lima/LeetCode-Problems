class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []

        for i in range(len(nums)):
            index = abs(nums[i]) - 1

            if nums[index] < 0:
                duplicates.append(index + 1)

            nums[index] = - nums[index]

        return duplicates
