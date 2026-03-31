class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        iterator = [0,0]
        iterator2 = [0, len(mat[0])-1]
        res = 0
        visited = set()
        
        while iterator != [len(mat), len(mat)]:
            iteration = [iterator[0],iterator[1]]
            iteration2 = [iterator2[0],iterator2[1]]
            if tuple(iteration) not in visited:
                print(iteration)
                res+=mat[iteration[0]][iteration[1]]
            if iteration != iteration2:
                res+=mat[iteration2[0]][iteration2[1]]
            visited.add(tuple(iteration))
            iterator[0]+=1
            iterator[1]+=1
            iterator2[0]+=1
            iterator2[1]-=1
    
        return res