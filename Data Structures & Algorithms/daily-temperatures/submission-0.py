class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures) 
        for i in range(len(temperatures)):
            count = 1
            for j in range(i+1, len(temperatures)):
                print(j)
                print(temperatures[i],":",temperatures[j])
                print(temperatures[i] >= temperatures[j])
                if temperatures[i] >= temperatures[j]:
                    count+=1
                else:
                    result[i] = count
                    break
        return result