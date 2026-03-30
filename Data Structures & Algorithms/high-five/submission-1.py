class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        id_to_grades = {}
        res = []
        for grade in items:
            if grade[0] not in id_to_grades:
                id_to_grades[grade[0]] = [grade[1]]
            else:
                id_to_grades[grade[0]].append(grade[1])
            
        sorted_ids=sorted(id_to_grades)
        print(id_to_grades)
        for id in sorted_ids:
        
            id_to_grades[id].sort()
            
            average = sum(id_to_grades[id][-1:-6:-1])//5
            res.append([id, average])
        return res