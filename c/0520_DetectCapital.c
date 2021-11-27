// Problem: Detect Capital (https://leetcode.com/problems/detect-capital/)
// Difficulty: Easy
// Date: 2021-11-27

/*
We define the usage of capitals in a word to be right when one of the following
cases holds:

All letters in this word are capitals, like "USA". All letters in this word are
not capitals, like "leetcode". Only the first letter in this word is capital,
like "Google". Given a string word, return true if the usage of capitals in it
is right.
*/

bool detectCapitalUse(char * word){
    int i = 0;
    bool hasFirstUpper = false;
    bool hasMultipleUpper = false;
    while(word[i] != '\0') {    
        if (isupper(word[i])) {
            if (!hasFirstUpper) {
                hasFirstUpper = true;
            } else {
                hasMultipleUpper = true;
            }
            
            if (i > 0 && islower(word[i - 1])) return false; // case: LeETCODE
        } else if (hasMultipleUpper) return false; // case: LEETCODe
        i++;
    }
    return true;
}