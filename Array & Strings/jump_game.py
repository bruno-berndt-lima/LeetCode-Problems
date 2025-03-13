class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        curr_position = goal - 1

        for curr_position in range(len(nums) - 2, -1, -1):
            if curr_position + nums[curr_position] >= goal:
                goal = curr_position           

        return True if goal == 0 else False
