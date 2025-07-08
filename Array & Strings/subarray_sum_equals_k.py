class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr_sum = n_subarrays = 0
        prefix_sums_freq = {0:1}
        
        for num in nums:
            curr_sum += num
            diff = curr_sum - k

            n_subarrays += prefix_sums_freq.get(diff, 0)
            prefix_sums_freq[curr_sum] = 1 + prefix_sums_freq.get(curr_sum, 0)
            
        return n_subarrays
