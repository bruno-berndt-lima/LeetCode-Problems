class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int current_index_sum = nums[0], overall_max_sum = nums[0];

        // Kadane's algorithm
        for(int i = 1; i < nums.size(); i++) {
            current_index_sum = max(nums[i], current_index_sum + nums[i]);
            overall_max_sum = max(overall_max_sum, current_index_sum);
        }
        return overall_max_sum;
    }
};
