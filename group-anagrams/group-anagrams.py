class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sett = {}
        res = []
        cnt = 0
        for word in strs:
            ww = sorted(word)
            ww = "".join(ww)
            if ww not in sett:
                sett[ww] = cnt
                res.append([word])
                cnt += 1
            else:
                res[sett[ww]].append(word)
        return res
            
            
                
        