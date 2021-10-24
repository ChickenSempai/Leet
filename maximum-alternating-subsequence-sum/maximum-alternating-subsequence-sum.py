class Solution:

    def alter(self, nums, n) -> (int, int, int, int):
        if n == len(nums)-1:
            return (nums[n], -nums[n], 0, 0)
        take, takeven, notake, notakeven = self.alter(nums, n+1)
        return max(takeven + nums[n], notakeven + nums[n]), max(take - nums[n], notake - nums[n]), max(take, notake) , max(takeven, notakeven)
                 
    def maxAlternatingSum(self, nums: List[int]) -> int:
        take, takeven, notake, notakeven = self.alter(nums, 0)
        return max(take, notake,notake, notakeven)
    

        