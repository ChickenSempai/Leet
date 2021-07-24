
class Solution:
    def subarraysWithKDistinct(self, nums, n):
        return self.atMostK(nums, n) - self.atMostK(nums, n - 1)

    def atMostK(self, nums, n):
        count = collections.Counter()
        res = left = 0
        for right in range(len(nums)):
            if count[nums[right]] == 0: 
                n -= 1
            count[nums[right]] += 1
            while n < 0:
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    n += 1
                left += 1
            res += right - left + 1
        return res