class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        L = 0
        avg = 0
        count=0
        for R in range(len(arr)):
            avg += arr[R]
            if R - L + 1 >= k:
                realAvg = avg // k
                print(realAvg)
                if realAvg >= threshold:
                    count+=1
                avg -= arr[L]
                L+=1
        return count