class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bottom = 0, ROWS-1
        searchRow = 0
        while top <= bottom:
            midRow = top + (bottom-top) // 2
            if target < matrix[midRow][0]:
                bottom = midRow - 1
            elif target > matrix[midRow][-1]:
                top = midRow + 1
            else:
                searchRow = midRow
                break

        L, R = 0, COLS-1
        while L <= R:
            mid = L + (R - L) // 2
            if matrix[searchRow][mid] < target:
                L = mid + 1
            elif matrix[searchRow][mid] > target:
                R = mid - 1
            else:
                return True
        return False
