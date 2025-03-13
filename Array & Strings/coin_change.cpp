class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        // Create an array dp[i] to store the minimum number
        // of coins needed to each value i until the amount desired
        vector<int> dp(amount + 1, INT_MAX - 1);
        
        // Number of coins needed to make amount 0 is 0
        dp[0] = 0; 

        for(int i = 1; i <= amount; i++) {
            for(int j = 0; j < coins.size(); j++) {
                // Check if is possible to subtract the coin from the amount
                if(i - coins[j] >= 0) {
                    // Update dp[i] to the minimum of its current value and (1 + dp[i - coins[j]])
                    dp[i] = min(dp[i], 1 + dp[i - coins[j]]);
                }
            }
        }
        
        return dp[amount] != (INT_MAX - 1) ? dp[amount] : -1;
    }
};
