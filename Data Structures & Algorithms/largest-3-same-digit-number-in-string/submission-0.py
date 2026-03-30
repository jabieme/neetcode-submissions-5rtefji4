class Solution:
    def largestGoodInteger(self, num: str) -> str:
        end = 2
        largest=""
        for start in range(len(num)):
            if end < len(num):
                cur = num[start]+num[start+1]+num[end]
                if num[start] == num[start+1] and num[start+1]==num[end]:
                    if not largest or int(largest[0]) < int(cur[0]):
                        largest = cur                 
                end+=1
        return largest