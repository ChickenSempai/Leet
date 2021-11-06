class Solution:
    pp = {}
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        self.pp.clear()
        return self.move(nums1, nums2, 0, 0)
    
    def move(self, nums1, nums2, up, down):
        if (up, down) in self.pp:
            return self.pp[(up, down)]
        maxS = 0
        if up == len(nums1) or down == len(nums2) : return 0
        for j in range(down, len(nums2)):
            if nums1[up] == nums2[j]:
                    maxS = max( maxS , 1 + self.move(nums1, nums2, up + 1, j + 1))
        maxS = max( maxS , self.move(nums1, nums2, up + 1, down))                    
        self.pp[(up, down)] = maxS
        return maxS