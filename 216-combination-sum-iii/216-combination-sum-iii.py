class Solution:
    ress = []
    
    def iterate(self, acts, k, val, n):
        
        if k >= len(acts):
            summ = 0
            for v in acts:
                summ+=v
            if summ == n:
                self.ress.append(acts.copy())
            return
        acts[k]=val
        for i in range(acts[k], 10):
            acts[k] = i
            self.iterate(acts, k+1, acts[k]+1, n)
    
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.ress = []
        actors = [i for i in range(1,k+1)]
        self.iterate(actors, 0, 1, n)
        return self.ress