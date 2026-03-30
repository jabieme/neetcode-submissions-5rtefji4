class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numFreqs = {}
        result = list()
        for num in nums:
            if num in numFreqs:
                numFreqs[num] = numFreqs[num] + 1
            else:
                numFreqs[num] = 1
        topK = sorted(numFreqs, key=numFreqs.get, reverse=True)
        i=0
        while i < k:
            result.append(topK[i])
            i = i+ 1
        return result
        