class Solution:
    def partition(self, ss: str) -> List[List[str]]:
        sdict = {}
        def rec(s):
            # if s in sdict:
                # return sdict[s]
            resarr = []
            if len(s) == 1:
                return [[s]]
            if len(s) == 0:
                return []
            for i in range(1,len(s)+1):
                if s[0:i] == s[i-1::-1]:
                    for r in rec(s[i:len(s)]):
                        resarr.append([s[0:i]]+r)
                    if len(s[i:len(s)]) == 0:
                        resarr.append([s[0:i]])
            # sdict[s] = resarr
            return resarr
        
        return rec(ss)