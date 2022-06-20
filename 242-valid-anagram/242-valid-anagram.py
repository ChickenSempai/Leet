class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c = Counter()
        if len(t)>len(s):
            temp = s
            s = t
            t = temp
        for i in range(len(s)):
            c[s[i]]+=1
        for i in range(len(t)):
            c[t[i]]-=1
            if c[t[i]] == 0:
                del c[t[i]]
        return len(c)==0
