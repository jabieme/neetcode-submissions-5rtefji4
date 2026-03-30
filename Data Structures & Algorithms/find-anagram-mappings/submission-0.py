class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num2Map = {}
        res = []
        for i in range(len(nums2)):
            if nums2[i] not in num2Map:
                num2Map[nums2[i]] = i
        
        for num in nums1:
            res.append(num2Map[num])
        return res