class Solution:
    
    def numSplits(self, s: str) -> int:
        ls={}
        rs={}
        cnt = 0
        for w in s:
            if w not in rs:
                rs[w]=1
            else:
                rs[w]+=1
        for w in s:
            rs[w]-=1
            if rs[w]==0:
                rs.pop(w)
            if w not in ls:
                ls[w]=1
            if len(ls) == len(rs):
               cnt+=1 
        return cnt