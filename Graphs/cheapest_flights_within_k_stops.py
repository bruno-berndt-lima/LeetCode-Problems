class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = [[] for _ in range(n)]
        for flight in flights:
            adj_list[flight[0]].append((flight[1], flight[2]))
                
        queue = deque([(src, 0)])
        min_cost = [float('inf') for _ in range(n)]
        stops = 0

        while queue and stops <= k:
            q_size = len(queue)
            for i in range(q_size):
                curr_node, cost = queue.popleft()
                for neighbour, price in adj_list[curr_node]:
                    if price + cost >= min_cost[neighbour]:
                        continue
                    min_cost[neighbour] = price + cost
                    queue.append((neighbour, min_cost[neighbour]))
            stops += 1

        return -1 if min_cost[dst] == float('inf') else min_cost[dst]
