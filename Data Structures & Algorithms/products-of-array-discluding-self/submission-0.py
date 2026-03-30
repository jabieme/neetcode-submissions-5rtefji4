class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        memory = []
        for i in range(len(nums)):
            print(memory)
            product=1
            for j in range(i+1, len(nums)):
                product*=nums[j]
            if len(memory) != 0:
                for num in memory:
                    product *= num
            memory.append(nums[i])
            nums[i] = product
            
        return nums
            

