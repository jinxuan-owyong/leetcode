// Problem: Implement strStr() (https://leetcode.com/problems/implement-strstr/)
// Difficulty: Easy
// Date: 2021-11-24

/*
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle
is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question
to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty
string. This is consistent to C's strstr() and Java's indexOf().
*/

bool is_substring(char* string, char* sub, int len_sub) {
    for (int x = 0; x < len_sub; x++) {
        if (string[x] != sub[x]) {
            return false;
        } 
    }
    return true;
}

int strStr(char * haystack, char * needle){
    int len_haystack = strlen(haystack);
    int len_needle = strlen(needle);
    
    if (len_needle == 0) {
        return 0;
    }
    
    for (int i = 0; i < len_haystack - len_needle + 1; i++) {
        if (haystack[i] == needle[0]) {
            if (is_substring(haystack + i, needle, len_needle)) {
                return i;
            }
        }
    } 
    return -1;
}