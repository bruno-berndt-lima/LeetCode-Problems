class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        int n = triangle.size();

        for(int i = n - 2; i >= 0; i--) {
            for(int j = 0; j <= i; j++) {
                // Starting from the penultimate row, sum value at index j of the current 
                // row with the values of position j and  j+1 of previous row and get the minimum of both
                triangle[i][j] += min(triangle[i + 1][j] , triangle[i + 1][j + 1] );
            }
        }
            
        return triangle[0][0];
    }
};
