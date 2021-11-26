// Problem: Length of Last Word (https://leetcode.com/problems/length-of-last-word/)
// Difficulty: Easy
// Date: 2021-11-27

/*
Given a string s consisting of some words separated by some number of spaces,
return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
*/

int lengthOfLastWord(char * s){
    int i = 0;
    int count = 0;
    while (s[i] != '\0') {
        // reset count when new word is reached
        if (i > 0 && s[i - 1] == ' ' && s[i] != ' ') count = 0;
        if (s[i] != ' ') count++;
        i++;
    }
    return count;
}
