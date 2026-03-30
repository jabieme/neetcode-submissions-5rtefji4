class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        end = min(len(s1), len(s2))-1
        res = []
        start = 0
        for i in range(len(s2)):
            if i - start > end:
                res.remove(s2[start])
                start+=1
            res.append(s2[i])
            if self.check(s1, res):
                return True
        return False
    
    def check(self, s: str, group: List[str]):
        valid = True

        hmap = Counter(group)
        amap = Counter(s)

        hmap = {k: v for k, v in sorted(hmap.items(), key=lambda item: item[1])}
        amap = {k: v for k, v in sorted(amap.items(), key=lambda item: item[1])}
        
        if amap == hmap:
            return True 
        return False
        