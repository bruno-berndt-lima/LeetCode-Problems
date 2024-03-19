class Solution {
public:
    int maxArea(vector<int>& height) {
        // Initialize two pointers
        int left = 0, right = height.size() - 1;
        int area = 0;

        while(left < right) {
            // Update the area if the current one is bigger than the previous
            area = max(area, min(height[right], height[left]) * (right - left));

            // Increase left if the current left height is lower than the right one
            if(height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }

        return area;
    }
};
