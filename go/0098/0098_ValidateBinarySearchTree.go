// 98. Validate Binary Search Tree

package main

import (
	"bufio"
	"fmt"
	"leetcode/structs"
	"leetcode/utils"
	"math"
	"os"

	"github.com/samber/lo"
)

func check(root *structs.TreeNode, lo int, hi int) bool {
	if root == nil {
		return true
	}
	if root.Val <= lo || root.Val >= hi {
		return false
	}
	// if we traverse left, then the upper limit is root.Val
	// traverse right, then lower limit is root.Val
	return check(root.Left, lo, root.Val) && check(root.Right, root.Val, hi)
}

func isValidBST(root *structs.TreeNode) bool {
	// BST is only valid if left subtree < root.Val < right subtree
	// alternatively perform inorder traversal and check for increasing values
	return check(root, math.MinInt, math.MaxInt)
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	var lines []string
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	const testSize int = 1

	for _, test := range lo.Chunk(lines, testSize) {
		root := utils.ToTree(test[0])
		result := isValidBST(root)
		fmt.Println(result)
	}
}
