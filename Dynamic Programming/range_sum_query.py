class NumArray:
    # Your NumArray object will be instantiated and called as such:
    # obj = NumArray(nums)
    # param_1 = obj.sumRange(left,right)

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.dp = [0] * (len(self.nums))

        self.dp[0] = self.nums[0]
        for i in range(1, len(nums)):
            self.dp[i] = self.nums[i] + self.dp[i - 1]

    def sumRange(self, left: int, right: int) -> int:
        l, r = left, right
        if left > 0:
            res = self.dp[right] - self.dp[left - 1]
        else:
            res = self.dp[right]

        return res

