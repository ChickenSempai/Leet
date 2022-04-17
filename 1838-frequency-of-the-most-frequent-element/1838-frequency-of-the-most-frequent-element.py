class Solution:
    def maxFrequency(self, nums, k: int) -> int:
        nums = sorted(nums)
        # print(nums)
        height_max = 0
        new_nums = nums.copy()
        for i in reversed(range(1, len(nums))):
            height_max += nums[i]-nums[i-1]
            new_nums[i-1] = height_max
        nums = new_nums
        nums[-1] = 0
        maxim = 1
        # print(len(nums))
        left = right = 0
        sliced_height = 0
        cur_sum = 0
        need_exit = False
        print(nums)
        while not need_exit:
            need_exit = True
            while right < len(nums) and cur_sum-(sliced_height*(right-left)) <= k:
                # print('#',cur_sum-(sliced_height*(right-left)))
                need_exit = False
                maxim = max(right-left+1, maxim)
                cur_sum += nums[right]
                # print(left, right)
                right += 1
                if  right < len(nums):
                    sliced_height = nums[right]
                else:
                    sliced_height = 0
            while left < len(nums) and cur_sum-(sliced_height*(right-left)) > k:
                # print(left, right)
                need_exit = False
                cur_sum -= nums[left]
                left += 1
        return maxim
