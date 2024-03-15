#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int n1 = nums1.size();
        int n2 = nums2.size();
        int n = n1 + n2;
        
        // Handle empty arrays
        if (n1 == 0) {
            if (n2 % 2 == 0)
                return (double)(nums2[n2 / 2 - 1] + nums2[n2 / 2]) / 2.0;
            else
                return nums2[n2 / 2];
        } else if (n2 == 0) {
            if (n1 % 2 == 0)
                return (double)(nums1[n1 / 2 - 1] + nums1[n1 / 2]) / 2.0;
            else
                return nums1[n1 / 2];
        }
        
        // Perform the binary search in the smaller array
        if (n1 > n2) 
            return findMedianSortedArrays(nums2, nums1); 

        int low = 0, high = n1;
        // Number of elements in the left half
        int leftHalfLength = (n1 + n2 + 1) / 2; 
        
        while (low <= high) {
            int partitionX = (low + high) / 2; // Partition of nums1

            // Calculate the partition of nums2 based on the length of the left half
            int partitionY = leftHalfLength - partitionX;

            // Calculate the maximum and minimum elements in the left and right partitions, if there a none assing INT_MIN or INT_MAX
            int maxLeftX = (partitionX == 0) ? INT_MIN : nums1[partitionX - 1];
            int minRightX = (partitionX == n1) ? INT_MAX : nums1[partitionX];
            int maxLeftY = (partitionY == 0) ? INT_MIN : nums2[partitionY - 1];
            int minRightY = (partitionY == n2) ? INT_MAX : nums2[partitionY];
            
            // Check if we have found the correct partition
            if (maxLeftX <= minRightY && maxLeftY <= minRightX) {
                // Check if the total number of elements is odd or even
                if (n % 2 == 0)
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0;
                else
                    return max(maxLeftX, maxLeftY);
            } else if (maxLeftX > minRightY) {
                // Move partition to the left in nums1
                high = partitionX - 1;
            } else {
                // Move partition to the right in nums1
                low = partitionX + 1;
            }
        }
        
        return -1;
    }
};
