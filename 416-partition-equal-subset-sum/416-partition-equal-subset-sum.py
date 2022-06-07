class Solution:
    
    dp = set()
    
    def rec(self, nums, i, newsum):
        if newsum == self.sum:
            return True
        if i>=len(nums) or newsum>self.sum:
            return False
        if newsum in self.dp:
            return False
        res = False
        res = res or self.rec(nums, i+1, newsum+nums[i])
        res = res or self.rec(nums, i+1, newsum)
        self.dp.add(newsum)
        return res
    
    def canPartition(self, nums: List[int]) -> bool:
        self.dp.clear()
        nums.sort(reverse=True)
        self.sum=0
        for n in nums:
            self.sum+=n
        self.sum = self.sum/2
        if self.sum != int(self.sum):
            return False

        return self.rec(nums,0,0)
    