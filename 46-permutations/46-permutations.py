class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def rec(nums, bitm, arr):
            perms = False
            for i in range(len(nums)):
                if not bitm & 1<<i:
                    perms = True
                    newbitm = bitm | (1 << i)
                    rec(nums, newbitm, arr + [nums[i]])             
            if perms == False:
                res.append(arr)
            return
        rec(nums,0,[])
        return res