// Problem: Pow(x, n) (https://leetcode.com/problems/powx-n/)
// Difficulty: Medium
// Date: 2021-11-24

/*
Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).
*/

double myPow(double x, int n){
    if (n == 0) {
        return 1; 
    }

    double result = 1;
    long power = n;
    if (n < 0) {
        x = 1/x;
        power = - (long) n;
    }
    
    double temp = myPow(x, power / 2); // O(log n), iterative solution takes too long - O(n)
    if (power % 2 == 0) {
       result = temp * temp; 
    } else {
       result = x * temp * temp; 
    }
    return result;
}