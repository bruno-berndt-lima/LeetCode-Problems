class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # Mark the numbers out of the range [0, n] with (n+1) value
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1

        # Mark each cell appearing in the array, by converting the index for that num to negative
        for i in range(n):
            index = abs(nums[i])
            if index > n:
                continue

            index -= 1
            if nums[index] > 0:
                nums[index] = -1 * nums[index]

        # Find the first cell which is not negative (i.e. does not appear in the array)
        for i in range(n):
            if nums[i] >= 0:
                return i + 1

        # If no positive num were found, it means the array contains all numbers 1..n
        return n + 1
