class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        index_map = {}
        res=[]
        for i in range(len(nums2)):
            if nums2[i] not in index_map:
                index_map[nums2[i]] = i
        print(index_map)
        for i in range(len(nums1)):
            res.append(index_map[nums1[i]])
        return res
