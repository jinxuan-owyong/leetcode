// Problem: Climbing Stairs (https://leetcode.com/problems/climbing-stairs/)
// Difficulty: Easy
// Date: 2021-11-24

/*
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you
climb to the top?
*/

int climbStairs(int n){
    if (n < 3) {
        return n;
    }
    
    long a = 1;
    long b = 2;
    long sum;
    
    for (int i = 3; i <= n; i++) { // basically fibonacci
        sum = a + b;
        a = b;
        b = sum;
    }
    
    return sum;
}