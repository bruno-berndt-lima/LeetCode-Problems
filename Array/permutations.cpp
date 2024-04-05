// Using next_permutation() from STL
class Solution_1 {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> permutations;
        permutations.push_back(nums);
        
        while(next_permutation(nums.begin(), nums.end())) {
            permutations.push_back(nums);
        } 

        return permutations;
    }
};

// Backtracking approach
class Solution_2 {
public:
    void permutations(vector<int>& nums, int i, int n, vector<vector<int>>& all_permutations) {
        if(i == n) {
            all_permutations.push_back(nums);
            return;
        }

        for(int j = i; j < n; j++) {
           swap(nums[i], nums[j]);
           permutations(nums, i + 1, n, all_permutations);
           swap(nums[i], nums[j]); 
        }
    }
    vector<vector<int>> permute(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>> all_permutations;
        permutations(nums, 0, n, all_permutations);
        
        return all_permutations;
    }
};
