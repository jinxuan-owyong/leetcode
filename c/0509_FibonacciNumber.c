// Problem: Fibonacci Number (https://leetcode.com/problems/fibonacci-number/)
// Difficulty: Easy
// Date: 2021-11-24

/*
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the
Fibonacci sequence, such that each number is the sum of the two preceding ones,
starting from 0 and 1. That is,

F(0) = 0, F(1) = 1 F(n) = F(n - 1) + F(n - 2), for n > 1. Given n, calculate
F(n).
*/


int fib(int n){
    if (n == 0) {
        return 0;
    }
    if (n < 3) {
        return 1;
    }
    return fib(n - 2) + fib(n - 1);
}