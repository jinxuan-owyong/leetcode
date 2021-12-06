// Problem: Rotate Image (https://leetcode.com/problems/rotate-image/)
// Difficulty: Medium
// Date: 2021-12-07

/*
You are given an n x n 2D matrix representing an image, rotate the image by 90
degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input
2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
*/

void swap(int** data, int x1, int y1, int x2, int y2) {
    int temp = data[x1][y1];
    data[x1][y1] = data[x2][y2];
    data[x2][y2] = temp;
}

void swapCorners(int** data, int leftBound, int rightBound) {
    swap(data, leftBound, leftBound, leftBound, rightBound); // top left and top right
    swap(data, leftBound, leftBound, rightBound, rightBound); // top right and bottom right
    swap(data, leftBound, leftBound, rightBound, leftBound); // bottom left and bottom right
}

void rotateEdges(int** data, int lowerBound, int upperBound) {
    // iterate through the number of edges and rotate the ith edge 90 degrees
    for (int i = 1; i < (upperBound - lowerBound); i++) {
        swap(data, lowerBound, lowerBound + i, lowerBound + i, upperBound);
        swap(data, lowerBound, lowerBound + i, upperBound, upperBound - i);
        swap(data, lowerBound, lowerBound + i, upperBound - i, lowerBound);
    }
}

void myRotate(int** matrix, int left, int right) {
    int size = right - left + 1;

    // base case 1: 1x1 grid
    if (size <= 1) return;
    // base case 2: 2x2 grid
    if (size == 2) {
        swapCorners(matrix, left, right);
        return;
    }

    // recursive case: rotate edges and corner
    swapCorners(matrix, left, right);
    rotateEdges(matrix, left, right);
    myRotate(matrix, left + 1, right - 1);
}

void rotate(int** matrix, int matrixSize, int* matrixColSize) {
    myRotate(matrix, 0, matrixSize - 1);
}

// Wrong Answer: incorrect logic in when rotating edges
// void rotateEdges(int** data, int lowerBound, int upperBound) {
//     // iterate through the number of edges
//     for (int i = lowerBound + 1; i < upperBound; i++) {
//         swap(data, lowerBound, i, i, upperBound);
//         swap(data, lowerBound, i, upperBound, upperBound - i);
//         swap(data, lowerBound, i, upperBound - i, lowerBound);
//     }
// }