class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        end = len(arr)-1
        maxNum = arr[end]
        while end >= 0:
            if end == len(arr)-1:
                arr[end] = -1
            elif arr[end] > maxNum:
                arr[end], maxNum = maxNum, arr[end]
            else:
                arr[end] = maxNum
            end-=1
        return arr