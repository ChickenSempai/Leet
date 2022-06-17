class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    
        def rec(first):
            if first == n:
                output.add(tuple(nums[:]))
            for i in range(first, n):
                if nums[first] != nums[i]:
                    nums[first], nums[i] = nums[i], nums[first]
                rec(first+1)
                if nums[first] != nums[i]:
                    nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        output = set()
        rec(0)
        return list(output)