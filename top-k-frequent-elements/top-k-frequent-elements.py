class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct = {}
        for i in nums:
            if i in dct:
                dct[i] += 1
            else: 
                dct[i] = 1
        return list(map(lambda x: x[0] ,sorted(dct.items(), key = lambda item: item[1], reverse = True)))[:k]