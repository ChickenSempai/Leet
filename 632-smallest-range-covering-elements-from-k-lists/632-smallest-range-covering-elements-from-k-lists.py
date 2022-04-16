class Solution:
    @staticmethod
    def compare(x, y):
        return x[0] - y[0]

    def smallestRange(self, nums):
        S = {}
        for i in range(len(nums)):
            for digit in nums[i]:
                if digit in S:
                    S[digit].add(i)
                else:
                    S[digit] = set()
                    S[digit].add(i)
        # print(S)
        space = sorted(S.items(), key=cmp_to_key(self.compare))
        left = right = 0
        color_set = {} #color -> count
        for color in space[0][1]:
            if color not in color_set:
                color_set[color] = 1
            else:
                color_set[color] += 1
        # print(space)
        min_sub = 10000000
        need_exit = False
        result=(0,0)
        while not need_exit:
            need_exit = True

            while len(color_set) < len(nums) and right < len(space)-1:
                # print(color_set, space[left][0], space[right][0])
                need_exit = False
                right += 1
                for color in space[right][1]:
                    if color not in color_set:
                        color_set[color] = 1
                    else:
                        color_set[color] += 1
            while len(color_set) == len(nums):
                # print(color_set, space[left][0], space[right][0])
                need_exit = False
                if space[right][0] - space[left][0] < min_sub:
                    min_sub=space[right][0] - space[left][0]
                    result=(space[left][0], space[right][0])
                for color in space[left][1]:
                    if color in color_set:
                        if color_set[color] > 0:
                            color_set[color] -= 1
                        if color_set[color] == 0:
                            color_set.pop(color)
                left += 1
        return result