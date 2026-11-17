class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Sorting an array based on the frequency of a hashmap.
        freqMap=Counter(nums)
        
        sorted_map = sorted(freqMap, key=lambda k: -freqMap[k])
        
        return sorted_map[0:k]