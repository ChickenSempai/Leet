class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = 0
        right= 1
        best = 0
        if len(nums)==0:
            return 0
        S = {nums[0]:1}
        summ=nums[0]
        while left<len(nums):
            
            if len(S) < right-left:
                S[nums[left]]-=1
                summ-=nums[left]
                if S[nums[left]]==0:
                    S.pop(nums[left])
                left+=1
            else:
                if right < len(nums):
                    best = max(best, summ)
                    summ+=nums[right]
                    if nums[right] not in S:
                        S[nums[right]] = 1
                    else:
                        S[nums[right]] += 1
                    right+=1
                else:
                    S[nums[left]]-=1
                    best = max(best, summ)
                    summ-=nums[left]
                    if S[nums[left]]==0:
                        S.pop(nums[left])
                    left+=1
                    
        return best
                