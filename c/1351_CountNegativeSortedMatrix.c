// Problem: Count Negative Numbers in a Sorted Matrix (https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/)
// Difficulty: Easy
// Date: 2021-11-24

/*
Given a m x n matrix grid which is sorted in non-increasing order both row-wise
and column-wise, return the number of negative numbers in grid.
*/


int countNegatives(int** grid, int gridSize, int* gridColSize){
    int count = 0;
    for (int i = *gridColSize - 1; i >= 0; i--) {
        for (int j = gridSize - 1; j >= 0; j--) {
            if (grid[j][i] < 0) {
                count++;
            } else break;
        }
    }
    return count;
}