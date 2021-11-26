// Problem: Reverse Integer (https://leetcode.com/problems/reverse-integer)
// Difficulty: Medium
// Date: 2021-11-23

/*
Given a signed 32-bit integer x, return x with its digits reversed. If reversing
x causes the value to go outside the signed 32-bit integer range [-231, 231 -
1], then return 0. Assume the environment does not allow you to store 64-bit
integers (signed or unsigned).
*/

#define LIMIT_10 214748364 // (2^31 - 1) / 10
#define LOWER -2147483648 // -2^31

int reverse(int x){
    if (x == LOWER) {
        return 0;
    }
    
    bool is_neg = x < 0;
    x = abs(x);
    int new = 0;
    bool found_first = false;
    
    while (x > 0) {
        int ones = x % 10;
        x /= 10;
        
        if (new > LIMIT_10) {
            return 0;
        }
        
        if (ones == 0 && !found_first) {
            continue;
        }
        
        found_first = true;
        new *= 10;
        new += ones;
    }
    
    return (is_neg ? -1 * new : new);
}