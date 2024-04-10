class Solution {
public:
    // Vector to stores all the subsets
    vector<vector<int>> solution;

    void generate_subsets(vector<int>& st, vector<int>& nums, int index) {
        // Base case: reach the end of nums
        if(index ==  nums.size()) {
            // Append the subset found to the solution
            solution.push_back(st);
            return;
        }
        // Include the current element of nums in the subset
        st.push_back(nums[index]);
        // Recursively generate subsets with the current element included
        generate_subsets(st, nums, index + 1);
        // Exclude the current element from the subset
        st.pop_back();
        // Recursively generate subsets with the current element excluded
        generate_subsets(st, nums, index + 1);
    }

    vector<vector<int>> subsets(vector<int>& nums) {
        vector<int> sst;
        generate_subsets(sst, nums, 0);

        return solution;
    }
};
