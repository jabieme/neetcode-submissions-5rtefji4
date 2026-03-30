class Solution:
    
    def countBits(self, n: int) -> List[int]:


        countLst = []

        for i in range(0, n+1):
            count=0
            binary = i
            
            while binary > 0:  
                if binary & 1 == 1:
                    count+=1
                binary = binary >> 1
            countLst.append(count)
        
        return countLst
