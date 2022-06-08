class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        trie = {}
        nums.sort()
        
        def rec(i, triet):
            if i == len(nums):
                return
            if nums[i] not in triet:
                triet[nums[i]]={}
            rec(i+1, triet[nums[i]])
            rec(i+1, triet)

        def recret(triet):
            if len(triet) == 0:
                return []
            res = []
            for i in triet:
                res.append([i])
                for reline in recret(triet[i]):
                    res.append([i]+reline)
                
            return res
        
        
        rec(0, trie)
        res = recret(trie)
        res.append([])
        return res