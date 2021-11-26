// Problem: Reverse String (https://leetcode.com/problems/reverse-string/)
// Difficulty: Easy
// Date:  2021-11-23

/*
Write a function that reverses a string. The input string is given as an array
of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.
*/

// Submission 1 (Less time)
void reverseString(char* s, int sSize){
    int i = 0;
    sSize--;
    while (i <= sSize) {
        char temp = s[i];
        s[i] = s[sSize];
        s[sSize] = temp;
        i++;
        sSize--;
    } 
}

// Sumbission 2 (Less memory)
void reverseString(char* s, int sSize){
    if (s[0] == '\0') {
        return;
    }
    char* front = s;
    char* back = s  - 1 + sSize;
    while (front <= back) {
        char temp = *front;
        *front = *back;
        *back = temp;
        front++;
        back--;
    } 
}