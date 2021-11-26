// Problem: Two Sum (https://leetcode.com/problems/two-sum/) 
// Difficulty: Easy
// Date: 2021-11-23

/*
Given an array of integers nums and an integer target, return indices of the two
numbers such that they add up to target. You may assume that each input would
have exactly one solution, and you may not use the same element twice. You can
return the answer in any order.
*/

int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    for (int i = numsSize - 1; i > 0; i--) {
        int required = target - nums[i];
        for (int j = i - 1; j >= 0; j--) {
            if (nums[j] == required) {
                int* result = malloc(2 * sizeof(int));
                if (result == NULL) {
                    return NULL;
                }
                
                result[0] = i;
                result[1] = j;
                *returnSize = 2;
                return result;
            }
        }
    }
    *returnSize = 0;
    return NULL;
}