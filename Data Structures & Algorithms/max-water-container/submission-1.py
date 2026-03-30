class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R = 0, len(heights)-1
        maxArea = 0
        print(len(heights))
        while L < R: 
            currArea = min(heights[L], heights[R]) * (R - L)
            maxArea = max(maxArea, currArea)
            if heights[L] < heights[R]:
                L+=1
            else:
                R-=1
        return maxArea