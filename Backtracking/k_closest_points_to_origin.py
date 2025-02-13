class Solution:
    def distance_to_origin(self, x, y):
        return math.sqrt(x ** 2 + y ** 2)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            # multiply by -1 to simulate max heap
            heapq.heappush(heap, (-self.distance_to_origin(x, y), (x, y)))
            
            if len(heap) > k:
                heapq.heappop(heap)

        return [point for _, point in heap]
