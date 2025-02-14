class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxheap = [-freq for freq in count.values()]
        heapq.heapify(maxheap)

        time = 0
        wait_queue = deque()

        while maxheap or wait_queue:
            time += 1

            if maxheap:
                # +1 because transformed in maxheap multiplying by -1
                task = 1 + heapq.heappop(maxheap)
                if task:
                    wait_queue.append((task, time + n))

            if wait_queue and wait_queue[0][1] == time:
                heapq.heappush(maxheap, wait_queue.popleft()[0])

        return time
