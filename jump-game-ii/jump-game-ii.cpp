
class Solution {
public:
    int jump(vector<int> nums) {
        int jumps = 0, currentJumpEnd = 0, farthest = 0;
        for (int i = 0; i < (nums.size() - 1); i++) {
            farthest = farthest > (i + nums[i]) ? farthest : nums[i]+i;
            if (i == currentJumpEnd) {
                jumps++;
                currentJumpEnd = farthest;
            }
        }
        return jumps;
    }
};

