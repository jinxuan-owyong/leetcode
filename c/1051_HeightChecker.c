// Problem: Height Checker (https://leetcode.com/problems/height-checker/)
// Difficulty: Easy
// Date: 2021-11-30

/*
A school is trying to take an annual photo of all the students. The students are
asked to stand in a single file line in non-decreasing order by height. Let this
ordering be represented by the integer array expected where expected[i] is the
expected height of the ith student in line.

You are given an integer array heights representing the current order that the
students are standing in. Each heights[i] is the height of the ith student in
line (0-indexed).

Return the number of indices where heights[i] != expected[i].
*/

void insert(int* arr, int pos) {
    int i = pos;
    int temp = arr[pos];
    while (i >= 1 && temp < arr[i - 1]) {
        arr[i] = arr[i - 1];
        i--;
    }
    arr[i] = temp;
}

void insertionSort(int* arr, int len) {
    for (int i = 1; i < len; i++) insert(arr, i);
}

int heightChecker(int* heights, int heightsSize) {
    if (heightsSize == 1) return 0;

    int* expected = malloc(heightsSize * sizeof(int));
    if (expected == NULL) return NULL;

    // duplicate heights
    for (int i = 0; i < heightsSize; i++) expected[i] = heights[i];
    insertionSort(expected, heightsSize);

    // count unmatched heights
    int count = 0;
    for (int i = 0; i < heightsSize; i++) {
        if (expected[i] != heights[i]) count++;
    }

    return count;
}