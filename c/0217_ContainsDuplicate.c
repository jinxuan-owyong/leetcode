// Problem: Contains Duplicate (https://leetcode.com/problems/contains-duplicate/)
// Difficulty: Easy
// Date: 2021-12-05

/*
Given an integer array nums, return true if any value appears at least twice in
the array, and return false if every element is distinct.
*/

// using qsort()
int comparator(const void* a, const void* b) {
    // determine the size of the int at a relative to b
    return *((int*)a) - *((int*)b);
}

bool containsDuplicate(int* nums, int numsSize) {
    qsort((void*)nums, numsSize, sizeof(nums[0]), comparator);

    // find duplicates
    for (int i = 0; i < numsSize; i++) {
        if (i > 0 && nums[i] == nums[i - 1]) return true;
    }

    return false;
}

// Time Limit Exceeded (19/20)
// void swap(int* arr, int a, int b) {
//     int temp = arr[a];
//     arr[a] = arr[b];
//     arr[b] = temp;
// }

// int findMin(int* arr, int pos, int len) {
//     for (int i = pos + 1; i < len; i++) {
//         if (arr[i] < arr[pos]) pos = i;
//     }
//     return pos;
// }

// bool containsDuplicate(int* nums, int numsSize) {
//     // using selection sort
//     for (int i = 0; i < numsSize - 1; i++) {
//         int min = findMin(nums, i, numsSize);
//         swap(nums, min, i);
//         // stops sorting once duplicate found
//         if (i > 0 && nums[i] == nums[i - 1]) return true;
//     }
//     // special case: last two elements are duplicates
//     return numsSize > 1 && nums[numsSize - 1] == nums[numsSize - 2];
// }
