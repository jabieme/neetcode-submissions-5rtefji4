class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] or grid[len(grid)-1][len(grid)-1]:
            return -1
        queue = deque()
        visit = set()
        
        queue.append((0,0,1))
        visit.add((0,0))

        ROWS, COLS = len(grid), len(grid[0])
        neighbors = [(0,1),(0,-1),(1,0),(-1,0),
                            (1,1),(-1,1),(1,-1), (-1,-1)]

        while queue:
            r, c, length = queue.popleft()
            if r == ROWS-1 and c == COLS-1:
                    return length

            for dr, dc in neighbors:
                if (min(r+dr, c+dc) >= 0 and 
                    r+dr < ROWS and c+dc < COLS and
                    (r+dr, c+dc) not in visit and grid[r+dr][c+dc] == 0):
                    
                    queue.append((r+dr, c+dc,length+1))
                    visit.add((r+dr, c+dc))
            
        return -1