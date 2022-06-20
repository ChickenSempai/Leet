class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs = [(''.join(sorted(strr)), strr) for strr in strs]
        strs.sort()
        word = strs[0][0]
        ans = [[]]
        wk = 0
        for st in strs:
            if st[0] == word:
                ans[wk].append(st[1])
            else:
                word = st[0]
                wk+=1
                ans.append([st[1]])
        return ans