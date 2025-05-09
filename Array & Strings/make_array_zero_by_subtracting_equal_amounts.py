class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        unique_elements = set([x for x in nums if x != 0])

        return len(unique_elements)
