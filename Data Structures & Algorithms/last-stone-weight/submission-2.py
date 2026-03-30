class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) >= 2:
            stones.sort()   
            print(stones)
            firstStone = stones.pop()
            secondStone = stones.pop()

            if firstStone > secondStone:
                stones.append(firstStone-secondStone)
            else: 
                stones.append(secondStone-firstStone)
        print(stones)
        return stones[0] if stones else 0