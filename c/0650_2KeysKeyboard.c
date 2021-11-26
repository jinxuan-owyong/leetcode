// Problem: 2 Keys Keyboard (https://leetcode.com/problems/2-keys-keyboard/)
// Difficulty: Medium
// Date: 2021-11-24

/*
There is only one character 'A' on the screen of a notepad. You can perform two
operations on this notepad for each step:

Copy All: You can copy all the characters present on the screen (a partial copy
is not allowed). Paste: You can paste the characters which are copied last time.
Given an integer n, return the minimum number of operations to get the character
'A' exactly n times on the screen.
*/

// iterative solution
bool isPrime(int n) {
    if (n <= 1) return false;
    if (n <= 3) return true;
    if (n % 2 == 0 || n % 3 == 0) return false;
    float limit = sqrt(n);
    for (int i = 5; i <= limit; i += 6) {
        if (n % i == 0 || n % (i + 2) == 0) return false;
    }
    return true;
}

int minSteps(int n){
    int steps = 0;
    while (n > 0) {
        if (n == 1) return steps;
        if (n == 2) return 2 + steps;
        if (isPrime(n)) return n + steps;

        int highest = 2;
        int i = 2;
        while (i < n) { // find divisor
            if (n % i == 0) {
                steps += i;
                break;
            }
            i++; 
        }
        n /= i; // if divisor found, n = remainder, otherwise divide by itself, n = 1
    }
    return steps;
}

// recursive solution (stack overflow)
bool isPrime(int n) {
    if (n <= 1) return false;
    if (n <= 3) return true;
    if (n % 2 == 0 || n % 3 == 0) return false;
    float limit = sqrt(n);
    for (int i = 5; i <= limit; i += 6) {
        if (n % i == 0 || n % (i + 2) == 0) return false;
    }
    return true;
}

int minSteps(int n){
    if (n == 1) return 0;
    if (n == 2) return 2;
    if (isPrime(n)) return n;
    
    int i = 2;
    int divisor = 1;
    
    while (i <= 10) {
       if (n % i == 0) {
           divisor = i;
           break;
       }
       i++;
    }
    
    return divisor + minSteps(n / divisor); 
}