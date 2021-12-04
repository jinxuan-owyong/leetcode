// Problem: Set Matrix Zeroes (https://leetcode.com/problems/set-matrix-zeroes/)
// Difficulty: Medium
// Date: 2021-12-04

/*
Given an m x n integer matrix matrix, if an element is 0, set its entire row and
column to 0's, and return the matrix.

You must do it in place.
*/

void setZeroes(int** matrix, int matrixSize, int* matrixColSize) {
    bool first_row_zero = false;
    bool first_col_zero = false;

    // find zeroes, store rows and columns to be set zero in the first row and column
    for (int i = 0; i < matrixSize; i++) {
        for (int j = 0; j < *matrixColSize; j++) {
            if (matrix[i][j] == 0) {
                if (i == 0) first_row_zero = true;
                if (j == 0) first_col_zero = true;
                matrix[i][0] = 0;
                matrix[0][j] = 0;
            }
        }
    }

    // set zeroes for rows
    for (int i = 1; i < matrixSize; i++) {
        if (matrix[i][0] == 0) {
            for (int j = 0; j < *matrixColSize; j++) {
                matrix[i][j] = 0;
            }
        }
    }

    // set zeroes for columns except first
    for (int j = 1; j < *matrixColSize; j++) {
        if (matrix[0][j] == 0) {
            for (int i = 0; i < matrixSize; i++) {
                matrix[i][j] = 0;
            }
        }
    }

    if (first_row_zero) {
        for (int j = 0; j < *matrixColSize; j++) {
            matrix[0][j] = 0;
        }
    }
    if (first_col_zero) {
        for (int i = 0; i < matrixSize; i++) {
            matrix[i][0] = 0;
        }
    }
}

// Wrong Answer: 
// Use of INT_MAX to mark whether rows/columns need to be zero
// Incorrect logic to determine whether to replace first row/column with zeroes
// void setZeroes(int** matrix, int matrixSize, int* matrixColSize) {
//     // find zeroes, store rows and columns to be set zero in the first row and column
//     for (int i = 0; i < matrixSize; i++) {
//         for (int j = 0; j < *matrixColSize; j++) {
//             if (matrix[i][j] == 0) {
//                 matrix[i][0] = INT_MAX;
//                 matrix[0][j] = INT_MAX;
//             }
//         }
//     }

//     // set zeroes for rows except first
//     for (int i = 1; i < matrixSize; i++) {
//         if (matrix[i][0] == INT_MAX) {
//             for (int j = 0; j < *matrixColSize; j++) {
//                 matrix[i][j] = 0;
//             }
//         }
//     }

//     // set zeroes for columns
//     bool top_left_zero = matrix[0][0] == INT_MAX;
//     for (int j = 0; j < *matrixColSize; j++) {
//         if (matrix[0][j] == INT_MAX) {
//             for (int i = 0; i < matrixSize; i++) {
//                 matrix[i][j] = 0;
//             }
//         }
//         if (top_left_zero) matrix[0][j] = 0;
//     }
// }