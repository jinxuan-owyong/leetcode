// Problem: Search Insert Position (https://leetcode.com/problems/search-insert-position/)
// Difficulty: Easy
// Date: 2021-11-23

/*
Given a sorted array of distinct integers and a target value, return the index
if the target is found. If not, return the index where it would be if it were
inserted in order.

You must write an algorithm with O(log n) runtime complexity.
*/

int searchInsert(int* nums, int numsSize, int target){
    int i = 0;
    int j = numsSize - 1;
    int mid;
    while (i <= j) {
        mid = (i + j) / 2;
        if (nums[mid] == target) { // exact match
            return mid;
        }
        if (nums[mid] > target) {
            j = mid - 1;
        } else {
            i = mid + 1;
        }
    }
    // where it would be if it were inserted in order
    return target < nums[mid] ? mid : mid + 1;
}