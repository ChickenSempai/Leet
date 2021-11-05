class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeros = {}
        oneCnt = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros[i] = oneCnt
                oneCnt = 0
            else: 
                oneCnt += 1
        zeros[len(nums)] = oneCnt
        maxSub = 0
        keys = []
        for key in zeros.keys():
            keys.append(key)
        if len(zeros) > 0:
            maxSub = zeros[keys[0]]
        for i in range(1, len(zeros)):
            maxSub = max(zeros[keys[i - 1]] + zeros[keys[i]], maxSub)
        if oneCnt == len(nums):
            return maxSub - 1
        return maxSub