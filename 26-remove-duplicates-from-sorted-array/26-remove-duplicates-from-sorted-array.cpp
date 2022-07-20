class Solution {
public:
    int removeDuplicates(std::vector<int>& nums) {
        int left=0, right=0;
        while(right < nums.size()){
            if (nums[right]>nums[left]){
                left++;
                nums[left]=nums[right];
                
            }
            right++;
        }
        return left+1;
    }
};