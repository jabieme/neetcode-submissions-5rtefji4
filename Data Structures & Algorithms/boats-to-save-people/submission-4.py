class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        numOfBoats = 0
        left, right = 0, len(people)-1

        while left <= right:
            if people[right] == limit:
                numOfBoats+=1
                right-=1
            elif people[right] + people[left] <= limit:
                numOfBoats+=1
                right-=1
                left+=1
            else:
                numOfBoats+=1
                right-=1
              
        return numOfBoats