// Problem: Remove Duplicates from Sorted Array (https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
// Difficulty: Medium
// Date: 2021-11-23

/*
Given an integer array nums sorted in non-decreasing order, remove the
duplicates in-place such that each unique element appears only once. The
relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you
must instead have the result be placed in the first part of the array nums. More
formally, if there are k elements after removing the duplicates, then the first
k elements of nums should hold the final result. It does not matter what you
leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the
input array in-place with O(1) extra memory.
*/

int removeDuplicates(int* nums, int numsSize){
    if (numsSize < 2) { // only one element
        return numsSize;
    }
    
    int k = 1; // k is the counts the number of unique elements
    
    for (int i = 1; i < numsSize; i++) {
        if (nums[i] == nums[i - 1]) continue; // skip any duplicates
        nums[k] = nums[i]; // copy unique
        k++;
    }
    
    return k;
}