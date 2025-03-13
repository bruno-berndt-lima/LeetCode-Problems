class Solution {
public:
    vector<vector<int>> generate(int num_rows) {
        // Vector to store the pascals triangle rows
        vector<vector<int>> pt_rows;

        // Base cases: 
        //  pt[0] = [1]      -> first row
        //  pt[1] = [1, 1]   -> second row
        pt_rows.push_back({1});
        if(num_rows == 1) return pt_rows;
        pt_rows.push_back({1, 1});
        if(num_rows == 2) return pt_rows;

        // Vector that stores each row
        vector<int> dp;
        for(int i = 2; i < num_rows; i++) {
            // Resize the vector to the current row size
            dp.resize(i + 1);
            
            // Calculate each element of the row using dynamic 
            // programming getting the values of previous rows
            for(int j = 1; j < i;j++){
                dp[j] = pt_rows[i - 1][j] + pt_rows[i - 1][j - 1];
            }
            
            // Base cases
            dp[0] = 1;
            dp[i] = 1;

            // Append the current row
            pt_rows.push_back(dp);
        }
        return pt_rows;
    }
};
