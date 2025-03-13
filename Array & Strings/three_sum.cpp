class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());

        int n = nums.size();
        vector<vector<int>> triplets;
        for (int i = 0; i < n - 2; i++) {
            // Check if the current element is not the same 
            // as the previous one (to avoid duplicates)
            if (i == 0 || (i > 0 && nums[i] != nums[i - 1])) {
                // Define the current target to sum 0 plus two other numbers
                int target = -nums[i];
                // Define two pointers
                int left = i + 1, right = n - 1;

                while (left < right) {
                    int sum = nums[left] + nums[right];
                    if (sum == target) {
                        triplets.push_back({nums[i], nums[left], nums[right]});
                        // Skip duplicates for the left and right pointers
                        while (left < right && nums[left] == nums[left + 1]) left++;
                        while (left < right && nums[right] == nums[right - 1]) right--;
                        left++;
                        right--;
                    } else if (sum < target) {
                        left++;
                    } else {
                        right--;
                    }
                }
            }
        }
        return triplets;
    }
};
