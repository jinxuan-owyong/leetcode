// Problem: Decompress Run-Length Encoded List (https://leetcode.com/problems/decompress-run-length-encoded-list/)
// Difficulty: Easy
// Date: 2021-12-07

/*
We are given a list nums of integers representing a list compressed with
run-length encoding.

Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]]
(with i >= 0).  For each such pair, there are freq elements with value val
concatenated in a sublist. Concatenate all the sublists from left to right to
generate the decompressed list.

Return the decompressed list.
*/

int* decompressRLElist(int* nums, int numsSize, int* returnSize) {
    int len = 0;
    for (int i = 0; i < numsSize; i += 2) len += nums[i];

    int* decompressed = malloc(len * sizeof(int));
    if (decompressed == NULL) {
        *returnSize = 0;
        return NULL;
    }

    int pos = 0;
    for (int i = 1; i < numsSize; i += 2) {
        for (int j = 0; j < nums[i - 1]; j++) {
            decompressed[pos] = nums[i];
            pos++;
        }
    }

    *returnSize = len;
    return decompressed;
}