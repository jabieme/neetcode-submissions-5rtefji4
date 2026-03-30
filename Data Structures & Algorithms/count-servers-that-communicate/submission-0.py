class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        rowCount = [0] * ROWS
        colCount = [0] * COLS
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    rowCount[r] += 1
                    colCount[c] += 1
        
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    if rowCount[r] > 1 or colCount[c] > 1:
                        res += 1
        return res