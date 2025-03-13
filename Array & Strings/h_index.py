class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort()

        for i, citation in enumerate(citations):
            if n - i <= citation:
                return n - i

        return 0
