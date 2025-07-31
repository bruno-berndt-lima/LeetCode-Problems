class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = [(p, s) for p, s in zip(position, speed)]
        pos_speed.sort()

        stack = []
        for pos, spd in pos_speed:
            time = (target - pos) / spd
            
            while stack and time >= stack[-1]:
                stack.pop()

            stack.append(time)

        return len(stack)
