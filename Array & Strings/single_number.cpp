class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int result = nums[0];
        for(int i = 1; i < nums.size(); i++) {
            // Perform the XOR operator between all numbers of the array, 
            // if there is a value that is single, it will be the result,
            // because A^A = 0, and 0^A = A
            result ^= nums[i];
        }
        return result;
    }
};
