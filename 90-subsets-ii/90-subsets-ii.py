class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        powerset = set()
        nums.sort()
        def rec(i, subset):
            if i == len(nums):
                powerset.add(tuple(subset))
                return
            rec(i+1, subset+[nums[i]])
            rec(i+1, subset)
        
        rec(0, [])
        return list(powerset)