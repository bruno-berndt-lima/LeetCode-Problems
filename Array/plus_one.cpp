class Solution {
public:
    void shift_right(vector<int>& digits) {
        for(int i = digits.size() - 1; i > 0; i--) {
            digits[i] = digits[i-1];
        }
    }
    vector<int> plusOne(vector<int>& digits) {
        int n = digits.size() - 1;
        while(true) {
            if(digits[n] != 9) {
                digits[n]++;;
                return digits;
            }
            digits[n] = 0;
            
            if(n == 0) {
                digits.resize(digits.size() + 1);
                shift_right(digits);
                digits[0] = 1;
                return digits;
            }

            n--;
        }
        return digits;
    }
};
