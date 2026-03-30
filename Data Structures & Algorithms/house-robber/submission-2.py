class Solution:
    def rob(self, nums: List[int]) -> int:
        prefixSum = []
        oddTotal = 0
        evenTotal = 0

        for i in range(len(nums)):
            if i % 2 == 0: 
                evenTotal = max(evenTotal + nums[i], oddTotal)
                prefixSum.append(evenTotal)
            else:
                oddTotal = max(oddTotal + nums[i], evenTotal)
                prefixSum.append(oddTotal)
        
        return max(prefixSum[-1], prefixSum[-2]) if len(prefixSum) > 1 else prefixSum[0]