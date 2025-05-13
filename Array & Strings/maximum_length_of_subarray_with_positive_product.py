class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        positive = negative = 0
        max_len = 0
        for num in nums:
            if num == 0:
                positive = 0
                negative = 0
            elif num > 0:
                positive += 1
                negative = 0 if negative == 0 else negative + 1
            else:
                positive, negative = 0 if negative == 0 else negative + 1, positive + 1

            max_len = max(max_len, positive)

        return max_len
