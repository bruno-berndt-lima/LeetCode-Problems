class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int break_point = -1;

        // Find the index of the break point where starting
        // from the end of the array, nums[i] < nums[i+1]
        for(int i =  nums.size() - 2; i >= 0; i--) {
            if(nums[i] < nums[i + 1]) {
                break_point = i;
                break;
            }
        }

        // If no break point found, this means that the array are 
        // sorted in decreasing order, then the next permutation
        // will be the array sorted in increasing order
        if(break_point == -1) {
            reverse(nums.begin(), nums.end());
        } else {
            int larger_num_index;
            for(int i = nums.size() - 1; i >= 0; i--) {
                // If there's a break point, starting from the end of the array,
                // find the index of the first value larger than the break point 
                if(nums[i] > nums[break_point]) {
                    larger_num_index = i;
                    // Swap the break point value with the first larger value found
                    swap(nums[break_point], nums[larger_num_index]);
                    // Finally, reverse the right side of break point 
                    reverse(nums.begin() + break_point + 1, nums.end());
                    break;
                }
            }
        }
    }
};
