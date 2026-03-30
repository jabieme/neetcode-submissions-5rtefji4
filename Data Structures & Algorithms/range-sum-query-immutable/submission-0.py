class NumArray:

    def __init__(self, nums: List[int]):
        preSum = []
        total=0
        for num in nums:
            total+=num
            preSum.append(total)

        self.prefixSum = preSum

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefixSum[right]
        else:
            return self.prefixSum[right]-self.prefixSum[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)