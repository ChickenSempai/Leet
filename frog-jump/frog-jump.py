class Solution:
    pp = set()

    def canCross(self, stones: List[int]) -> bool:
        self.pp.clear()
        if (len(stones)) > 1:
            if stones[0] != stones[1] - 1: return False
        return self.reach(stones, 1, 1)
        
    def reach(self, stones, cSI, cJ):
        if (cSI, cJ) in self.pp:
            return False
        if cSI == len(stones) - 1: return True
        for i in range(cSI + 1, len(stones)):
            if (stones[i] - 1) <= (stones[cSI] + cJ) <= (stones[i] + 1):
                if self.reach(stones, i, stones[i] - stones[cSI]):
                    return True
            else:
                if (stones[cSI] + cJ) < (stones[i] - 1):
                    break
        self.pp.add( (cSI, cJ) )
        return False