class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def permut(self, setN, index, res):
            setN = setN.copy()
            if index == len(nums):
                result.append(setN)
                return
            permut(self,setN, index + 1, res)
            setN.append(nums[index])
            permut(self, setN, index + 1, res)
            return
        
        permut(self,[],0, result)
        return result
    
    