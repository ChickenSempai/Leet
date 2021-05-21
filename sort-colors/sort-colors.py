class Solution:
    def sortColors(self, nums: List[int]) -> None:
        bucket = Counter(nums)
        nums[:bucket[0]] = [0 for x in range(bucket[0])]
        nums[bucket[0]:bucket[0] + bucket[1]] = [1 for x in range(bucket[1])]
        nums[bucket[0] + bucket[1]:len(nums)] = [2 for x in range(bucket[2])]
        