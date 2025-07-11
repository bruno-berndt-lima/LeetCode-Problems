class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        min_boats = 0
        people.sort()

        l, r = 0, len(people) - 1
        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
            r -= 1
            min_boats += 1
            
        return min_boats
