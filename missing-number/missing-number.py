class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i] += 1
        for num in nums:
            if abs(num)-1 < len(nums):
                nums[abs(num)-1] = - nums[abs(num)-1]
        for i in range(len(nums)):
            if nums[i] > 0:
                return i
        return len(nums) 
        