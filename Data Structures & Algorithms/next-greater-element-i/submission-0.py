class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {}
        res = []
        for i in range(len(nums2)):
            for j in range(i, len(nums2)):
                if nums2[i]<nums2[j]:
                    hashmap[nums2[i]]=nums2[j]
                    break

        for num in nums1:
            if num in hashmap:
                res.append(hashmap[num])
            else:
                res.append(-1)
        return res