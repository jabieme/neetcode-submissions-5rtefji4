class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bot = 0, ROWS-1
        searchedRow = 0
        while top <= bot:
            mid = top + (bot-top) // 2
            if matrix[mid][-1] < target:
                top = mid + 1
            elif matrix[mid][0] > target:
                bot = mid - 1
            else:
                searchedRow = mid
                break
        
        L, R = 0, COLS-1
        while L <= R:
            mid = L + (R - L) // 2
            if matrix[searchedRow][mid] < target:
                L = mid + 1
            elif matrix[searchedRow][mid] > target:
                R = mid - 1
            else:
                return True
        return False