class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freqMap = Counter(arr)
        res = []

        for char in arr:
            if freqMap[char] == 1:
                res.append(char)
        return res[k-1] if k <= len(res) else ""