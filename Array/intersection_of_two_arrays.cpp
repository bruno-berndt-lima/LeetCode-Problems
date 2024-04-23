class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        set<int> set1 (begin(nums1), end(nums1));
        set<int> set2 (begin(nums2), end(nums2));
        vector<int> intersec;
        for (int num : set1) {
            if (set2.find(num) != set2.end()) {
                intersec.push_back(num);
            }
        }
        return intersec;

    }
};
