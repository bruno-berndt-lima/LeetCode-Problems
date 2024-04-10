class Solution {
public:
    int majorityElement(vector<int>& nums) {
        // Map to count the occurrences of a number
        unordered_map<int, int> nums_occurrences;
        int n = nums.size();

        // If the number is not in the map, add it and 
        // increase the count else just increase the count
        for(int i = 0; i < n; i ++) {
            nums_occurrences[nums[i]]++;
        } 

        int m = n / 2;

        for(auto n : nums_occurrences) {
            // If the num of occurrences is bigger 
            // than half of the array, return the number
            if(n.second > m) {
                return n.first;
            }
        }
         return 0;
    }
};
