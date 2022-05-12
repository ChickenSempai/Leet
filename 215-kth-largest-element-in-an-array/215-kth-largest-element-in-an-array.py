class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        vals = [0 for x in range(20002)]
        for n in nums:
            vals[n+10001] += 1
        for i in reversed(range(len(vals))):
            if vals[i]:
                k -= vals[i]
                if k<=0:
                    return i-10001