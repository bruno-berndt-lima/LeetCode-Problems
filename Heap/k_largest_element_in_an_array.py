class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # using nlargest built in function from heapq library
        # k_largest = heapq.nlargest(k, nums)[k-1]
        
        min_heap = []

        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        k_largest = min_heap[0]

        return k_largest
