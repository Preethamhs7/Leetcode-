class Solution {
public:
    int romanToInt(string s) {
        int sum = 0;
        int prevValue = 0;
        unordered_map<char, int> value = {
            {'I', 1}, {'V', 5}, {'X', 10}, {'L', 50},
            {'C', 100}, {'D', 500}, {'M', 1000}
        };

        for (char c : s) {
            int curValue = value[c];
            sum += (curValue > prevValue) ? (curValue - 2 * prevValue) : curValue;
            prevValue = curValue;
        }
        return sum;
    }
};
