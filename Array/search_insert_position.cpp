class Solution {
public:
    int binary_search(vector<int>& nums, int target, int left, int right) {
        int mid = (right + left) / 2;
        if(left >= right) {
            if(nums[mid] < target) return mid + 1;
            if(nums[mid] > target) return mid;
        }
        
        if(nums[mid] == target) {
            return mid;
        } else if(nums[mid] < target) {
            return binary_search(nums, target, mid + 1, right);
        } else {
            return binary_search(nums, target, left, mid - 1);
        }

    }
    int searchInsert(vector<int>& nums, int target) {
        int n = nums.size() - 1;
        int index = binary_search(nums, target, 0, n);

        return index;
    }
};
