// Problem: Jewels and Stones (https://leetcode.com/problems/jewels-and-stones/)
// Difficulty: Easy
// Date: 2021-12-11

/*
You're given strings jewels representing the types of stones that are jewels,
and stones representing the stones you have. Each character in stones is a type
of stone you have. You want to know how many of the stones you have are also
jewels.

Letters are case sensitive, so "a" is considered a different type of stone from
"A".
*/

int numJewelsInStones(char* jewels, char* stones) {
    int count = 0;
    while (*stones != '\0') {
        int i = 0;
        while (jewels[i] != '\0') {
            *stones == jewels[i] && count++;
            i++;
        }
        stones++;
    }
    return count;
}