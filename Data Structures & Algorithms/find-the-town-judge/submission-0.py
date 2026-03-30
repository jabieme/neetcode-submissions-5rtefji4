class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        judge = 0
        for person in trust:
            if judge == 0:
                judge = person[1]
            else:
                if person[1] != judge:
                    return -1
        return judge
