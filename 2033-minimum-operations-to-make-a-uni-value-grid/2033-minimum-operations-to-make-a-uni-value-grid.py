class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        S = {}
        minn = 100000
        diff = 0
        maxx = 0
        for l in grid:
            for g in l:
                minn=min(minn, g)
                maxx=max(maxx, g)
        cnt = 0
        for l in grid:
            for g in l:  
                cnt+=1
                if g not in S:
                    S[g]=1
                else: 
                    S[g]+=1
                if (g-minn)%x!=0:
                    return -1
                diff += (g-minn)
                
        bcnt = cnt-S[minn]
        lcnt = S[minn]
        mindif = diff
        res =  0
        # print(bcnt)
        for i in range(minn+x, maxx+1, x):
            diff += x*lcnt-x*bcnt
            # print(diff)    
            if diff < mindif:
                mindif = diff
            if i in S:
                bcnt-=S[i]
                lcnt+=S[i]
        # print(bcnt, lcnt)    
        if bcnt != 0:
            return -1
        return mindif//x