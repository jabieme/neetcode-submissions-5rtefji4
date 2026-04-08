class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        pairs=[]
        for num, count in Counter(nums).items():
            pairs.append([num,count])
        def qsort(s,e):
            if e-s+1 <= 1:
                return pairs
            
            pivot = pairs[e]
            left=s

            for i in range(s,e):
                if pairs[i][1] < pivot[1] or (pairs[i][1] == pivot[1] and pairs[i][0] > pivot[0]):
                    tmp = pairs[i]
                    pairs[i]=pairs[left]
                    pairs[left]=tmp
                    left+=1

            pairs[e]=pairs[left]
            pairs[left]=pivot

            qsort(s,left-1)
            qsort(left+1,e)
            return pairs
        res=[]
        pairs = qsort(0,len(pairs)-1)
        for pair in pairs:
            for _ in range(pair[1]):
                res.append(pair[0])
        return res