// Problem: Search a 2D Matrix (https://leetcode.com/problems/search-a-2d-matrix/)
// Difficulty: Medium
// Date: 2021-12-18

/*
Write an efficient algorithm that searches for a value in an m x n matrix. This
matrix has the following properties:

Integers in each row are sorted from left to right. The first integer of each
row is greater than the last integer of the previous row.
*/

bool searchMatrix(int** matrix, int matrixSize, int* matrixColSize, int target) {
    matrixSize--;
    while (matrixSize >= 0) {
        // search for row with elements less than or equal to target
        if (matrix[matrixSize][0] > target) {
            matrixSize--;
        }
        else {
            // search row possibly containing target
            for (int i = 0; i < *matrixColSize; i++) {
                if (matrix[matrixSize][i] == target) return true;
            }
            // terminate search, target will not be found in remaining rows
            return false;
        }
    }
    return false;
}
