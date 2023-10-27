#include <vector>

using namespace std;

// O(N) solution
class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> result(n + 1, 0);
        // between 0 (inclusive) and i (non-inclusive)
        // there exists x, y in range(n); x = y / 2
        // => they have one differing bit
        // 000 -> 000
        // 001 -> 000
        // 010 -> 001
        // 011 -> 001
        // 100 -> 010
        // 101 -> 010
        // 111 -> 011
        // trivial: result[0] == 0
        for (int i = 1; i <= n; ++i) {
            // memoized result from i >> 1 (every bit except the LSB, divide by 2)
            // LSB == 1 <==> i is odd
            result[i] = result[i >> 1] + (i & 1);
        }
        return result;
    }
};

// O(N log N) solution
// class Solution {
// public:
//     vector<int> countBits(int n) {
//         vector<int> result(n + 1, 0);
//         for (int i = 0; i <= n; ++i) {
//             int curr = i;
//             while (curr) {
//                 if (curr & 1) { // mask ones bit
//                     --curr;
//                     ++result[i];
//                 }
//                 curr = curr >> 1;
//             }
//         }
//         return result;
//     }
// };
