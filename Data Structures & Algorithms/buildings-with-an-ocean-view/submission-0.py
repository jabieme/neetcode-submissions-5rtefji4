class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        view_stack = []

        for i in range(len(heights)):
            if view_stack and heights[view_stack[-1]] <= heights[i]:
                while view_stack and heights[view_stack[-1]] <= heights[i]:
                    view_stack.pop()
            view_stack.append(i)
        return view_stack