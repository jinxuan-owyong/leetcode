// Problem: Two Sum II - Input Array Is Sorted (https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
// Difficulty: Easy
// Date: 2021-11-23

/*
Given a 1-indexed array of integers numbers that is already sorted in
non-decreasing order, find two numbers such that they add up to a specific
target number. Let these two numbers be numbers[index1] and numbers[index2]
where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an
integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use
the same element twice.
*/


int* twoSum(int* numbers, int numbersSize, int target, int* returnSize){
    for (int i = 0; i < numbersSize; i++) {
        int required = target - numbers[i];
        for (int j = i + 1; j < numbersSize; j++) { // j=i+1 skips repeated checks
            if (numbers[j] > required) {
                break;
            }
            if (numbers[j] == required) {
                int* result = malloc(2 * sizeof(int));
                if (result == NULL) {
                    return NULL;
                }
                
                result[0] = i + 1;
                result[1] = j + 1;
                *returnSize = 2;
                return result;
            }
        }
    }
    *returnSize = 0;
    return NULL;
}