class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        res = [0]
        for num in num_set:
            if num-1 not in num_set:
                n=0
                count=0
                while num+n in num_set:
                    count+=1
                    n+=1
                res.append(count)
        
        return max(res)