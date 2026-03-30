class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        queue = deque()
        visit = set()
        if matrix[0][0] == target:
            return True
        if not matrix:
            return False

        queue.append((0,0))
        visit.add((0,0))
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        ROWS, COLS = len(matrix), len(matrix[0])
        while queue:
            r, c = queue.popleft()
            if r == ROWS-1 and c == COLS-1 and matrix[r][c] != target:
                return False
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if min(nr,nc) >= 0 and nr < ROWS and nc < COLS and matrix[nr][nc] not in visit and matrix[nr][nc] == target:
                    return True
                queue.append((nr,nc))
                visit.add((nr,nc))
        return False
