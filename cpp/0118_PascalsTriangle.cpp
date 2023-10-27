#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> result(numRows);
        // start and end of vectors have default value 1
        for (int i = 0; i < numRows; ++i) result[i] = vector<int>(i + 1, 1);
        for (int i = 1; i < numRows; ++i) {
            for (int j = 1; j < i; ++j) {
                result[i][j] = result[i - 1][j - 1] + result[i - 1][j];
            }
        }
        return result;
    }
};

int main() {
    Solution s;
    int n;
    cin >> n;
    auto result = s.generate(n);
    for (auto row : result) {
        for (auto col : row) {
            cout << col << ' ';
        }
        cout << '\n';
    }
}