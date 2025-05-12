class Solution:
    def reorganizeString(self, s: str) -> str:
        count_map = Counter(s)

        max_heap = [(-freq, char) for char, freq in count_map.items()]
        heapq.heapify(max_heap)

        new_s = ""
        prev_freq, prev_char = 0, ""
        while max_heap:
            freq, char = heapq.heappop(max_heap)
            new_s += char

            if prev_freq < 0:
                heapq.heappush(max_heap, (prev_freq, prev_char))

            freq += 1
            prev_freq, prev_char = freq, char

        if len(new_s) != len(s):
            return ""

        return new_s
