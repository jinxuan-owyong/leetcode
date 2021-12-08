// Problem: Merge Sorted Array (https://leetcode.com/problems/merge-sorted-array/)
// Difficulty: Easy 
// Date: 2021-12-09

/*
You are given two integer arrays nums1 and nums2, sorted in non-decreasing
order, and two integers m and n, representing the number of elements in nums1
and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be
stored inside the array nums1. To accommodate this, nums1 has a length of m + n,
where the first m elements denote the elements that should be merged, and the
last n elements are set to 0 and should be ignored. nums2 has a length of n.
*/

void swap(int* arr, int first, int second) {
    int temp = arr[first];
    arr[first] = arr[second];
    arr[second] = temp;
}

void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n) {
    m--;
    n--;
    nums1Size--;

    while (m >= 0 && n >= 0) {
        if (nums1[m] > nums2[n]) {
            nums1[nums1Size] = nums1[m];
            m--;
        }
        else {
            nums1[nums1Size] = nums2[n];
            n--;
        }
        nums1Size--;
    }

    // copy remaining numbers from nums2 to nums1, if any
    if (n >= 0) {
        while (n >= 0) {
            nums1[nums1Size] = nums2[n];
            nums1Size--;
            n--;
        }
    }
}
