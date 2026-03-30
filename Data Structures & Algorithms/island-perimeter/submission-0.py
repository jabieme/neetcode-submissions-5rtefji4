class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # equal to 0
        # greater than or lessen the length of rows or columns
        ROWS, COLS, = len(grid), len(grid[0])
        visited = set()
        bigCount = 0
        def dfs(r, c):
            count=4
            if r < 0 or c < 0 or COLS < c or ROWS < r:
                return 0
            elif grid[r][c] == 0 or ((r,c)) in visited:
                return 0
            visited.add((r,c))
            if grid[r][c] == 1:
                if r+1 < ROWS and grid[r+1][c] == 1:
                    count-=1
                if r-1 >= 0 and grid[r-1][c] == 1:
                    count-=1
                if c+1 < COLS and grid[r][c+1] == 1:
                    count-=1
                if c-1 >= 0 and grid[r][c-1] == 1:
                    count-=1
            print("("+str(r)+ ", " +str(c)+"): adds " + str(count))
            return count

        for row in range(len(grid)):
            for cell in range(len(grid[row])): 
                bigCount += dfs(row, cell)
        return bigCount


            
            



