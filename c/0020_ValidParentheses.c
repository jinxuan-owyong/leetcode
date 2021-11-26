// Problem: Valid Parentheses (https://leetcode.com/problems/valid-parentheses)
// Difficulty: Easy
// Date: 2021-11-24

/*
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets. 
2. Open brackets must be closed in the correct order.
*/

char matchingClose(char open) {
    char matching = 'X';
    switch (open) {
        case '(':
            matching = ')';
            break;
        case '{':
            matching = '}';
            break;
        case '[':
            matching = ']';
            break;
    }
    return matching;
}

bool isValid(char * s){
    int len = strlen(s);
    if (len % 2 != 0) return false;  // number of brackets not matching

    char* stack = malloc((len / 2) * sizeof(int));
    if (stack == NULL) {
        return false;
    }

    int x = 0;
    for (int i = 0; i < len; i++) {
        if (s[i] == '(' || s[i] == '{' || s[i] == '[') {
            // add open parentheses to stack
            stack[x] = s[i];
            x++;
        } else if (x > 0 && matchingClose(stack[x - 1]) == s[i]) {
            x--;
        } else return false; // open and close parentheses do not match
    }

    if (x == 0) return true; // no more open brackets remaining on the stack
    return false;
}