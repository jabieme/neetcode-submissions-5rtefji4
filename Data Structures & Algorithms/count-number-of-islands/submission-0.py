class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0,1], [0,-1], [1,0],[-1,0]]
        island=0

        def bfs(r, c):
            queue = deque()
            grid[r][c] = "0"
            queue.append((r,c))
            
            while queue:
                row,col = queue.popleft()
                for dr, dc in directions:
                    nr, nc = row+dr, col+dc
                    if (nr >= ROWS or nc >= COLS or 
                        min(nr,nc) < 0 or grid[nr][nc] == "0"):
                        continue
                    queue.append((nr,nc))
                    grid[nr][nc]="0"

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r,c)
                    island+=1
        return island
        