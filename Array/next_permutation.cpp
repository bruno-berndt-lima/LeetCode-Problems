class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int break_point = -1;

        for(int i =  nums.size() - 2; i >= 0; i--) {
            if(nums[i] < nums[i + 1]) {
                break_point = i;
                break;
            }
        }

        if(break_point == -1) {
            reverse(nums.begin(), nums.end());
        } else {
            int larger_num_index;
            for(int i = nums.size() - 1; i >= 0; i--) {
                if(nums[i] > nums[break_point]) {
                    larger_num_index = i;
                    swap(nums[break_point], nums[larger_num_index]);
                    reverse(nums.begin() + break_point + 1, nums.end());
                    break;
                }
            }
        }
    }
};
