class Solution:
    
    def rec(self, seti, pivot, nextnum, nums2):
        if nextnum == -1:
            return -1
        if pivot < nextnum:
            return nextnum
        else:
            return self.rec(seti, pivot, nums2[seti[nextnum]][1], nums2)
    
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        seti = {}
        for i,num in enumerate(nums2):
            seti[num]=i
        nums2[len(nums2)-1]=(nums2[len(nums2)-1], -1)
        for i in reversed(range(len(nums2)-1)):
            if nums2[i] < nums2[i+1][0]:
                nums2[i] = (nums2[i], nums2[i+1][0])
            else:
                nums2[i] = (nums2[i], self.rec(seti, nums2[i], nums2[i+1][1], nums2))
        for num in nums1:
            ans.append(nums2[seti[num]][1])
        return ans