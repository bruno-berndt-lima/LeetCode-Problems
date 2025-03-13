class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        // Make k be in the range(0, nums.size());
        k = k % nums.size();

        // Reverse the whole array
        reverse(nums.begin(), nums.end());
        // Reverse array in range(k, nums.size())
        reverse(nums.begin() + k, nums.end());
        // Reverse array in range(0, k)
        reverse(nums.begin(), nums.begin() + k);
    }
};
