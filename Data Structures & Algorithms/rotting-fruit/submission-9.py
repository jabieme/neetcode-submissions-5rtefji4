class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid),len(grid[0])
        if (ROWS==1 and COLS==1) and grid[ROWS-1][COLS-1] != 1:
            return 0
        def printGrid():
            for ROW in range(ROWS):
                print(grid[ROW])
        def bfs(origin):
            queue = deque()
            visit=set()
            for coord in origin:
                queue.append(coord)
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            minute=0
            while queue:
                level_size = len(queue)
                changed = False
                # print(queue)
                # print("visit",visit)
                
               
                printGrid()
                for _ in range(level_size):
                    r,c = queue.popleft()
                    for dr, dc in directions:
                        nr, nc = r+dr, dc+c
                        
                        print("Testing:",(nr,nc))
                        printGrid()
                        
                        if min(nr,nc)<0 or nr == ROWS or nc == COLS or grid[nr][nc] == 0 or grid[nr][nc]==2:
                            # print("Failed:",(nr,nc)) 
                            continue
                        elif grid[nr][nc] == 1:
                            changed = True
                            # print("Passed:",(nr,nc))
                            grid[nr][nc] = 2
                            queue.append((nr,nc))  
                            
                    # print("Adding 1 minute")
                if changed:
                    minute += 1
                
                # print((r,c),"added to visit")
                # print("visit:",visit)
                print("minutes accumulated:",minute)
                # print("\n")
            return minute
        distances = []
        for ROW in range(ROWS):
            for COL in range(COLS):
                if grid[ROW][COL] == 2:
                    distances.append((ROW, COL))
        result = bfs(distances)

        for ROW in range(ROWS):
            for COL in range(COLS):
                if grid[ROW][COL] == 1:
                    print("Returned Here")
                    return -1
        return result
        # for ROW in range(ROWS):
        #     print(grid[ROW])
        # return distance if distance != 0 else -1
