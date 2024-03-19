class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // Create a copy of nums which stores the number and the index
        vector<pair<int, int>> nums_copy;
        for(int i = 0; i < nums.size(); i++) {
            nums_copy.push_back({nums[i], i});
        }
        // Sort the new array
        sort(nums_copy.begin(), nums_copy.end());

        int i = 0, j = nums.size() - 1;

        // Loop through the sorted array comparing beginning and end, if matches the
        // target return both indexes, if the sum is lower increase i, else decrease j
        while(i < j) {
            if(nums_copy[i].first + nums_copy[j].first == target) {
              return {nums_copy[i].second, nums_copy[j].second};
            } else if(nums_copy[i].first + nums_copy[j].first < target) {
                i++;
            } else if(nums_copy[i].first + nums_copy[j].first > target) {
                j--;
            } 
        }
        return {};
    }
};
