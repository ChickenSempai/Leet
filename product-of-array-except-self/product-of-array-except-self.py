class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lefts = [1 for x in nums]
        rights = [1 for x in nums]
        for i in range(1,len(nums)):
            lefts[i] = lefts[i - 1] * nums[i - 1]
        for i in reversed(range(0, len(nums)- 1)):
            rights[i] = rights[i + 1] * nums[i + 1]
        
        return [lefts[i] * rights[i] for i in range(len(nums))]
        