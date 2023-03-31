#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> result;
        generateRecursively(n, n, result, "");
        return result;
    }

    void generateRecursively(int num_open, int num_close, vector<string>& result, string curr) {
        if (num_open == 0 && num_close == 0) {
            result.emplace_back(curr);
        }
        if (num_open > 0) {
            generateRecursively(num_open - 1, num_close, result, curr + "(");
        }
        if (num_close > 0 && num_open < num_close) {  // extra check to prevent start with close
            generateRecursively(num_open, num_close - 1, result, curr + ")");
        }
    }
};

int main(void) {
    int n;
    cin >> n;
    auto result = Solution().generateParenthesis(n);
    for (auto s : result) {
        cout << s << "\n";
    }
}
