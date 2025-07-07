import heapq
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        hashset = set(nums)

        for num in hashset:
            if num - 1 not in hashset:
                curr_len = 1
                while (num + curr_len) in hashset:
                    curr_len += 1
            
                max_len = max(max_len, curr_len)

        return max_len
