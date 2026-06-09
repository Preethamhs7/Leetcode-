class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        int n = nums.size();
        vector<int> result(n);
        int left = 0;
        int right = n - 1;
        int index = n - 1;

        while (left <= right) {
            int leftVal = abs(nums[left]);
            int rightVal = abs(nums[right]);

            if (leftVal > rightVal) {
                result[index] = leftVal * leftVal;
                left++;
            } else {
                result[index] = rightVal * rightVal;
                right--;
            }
            index--;
        }

        return result;
    }
};
