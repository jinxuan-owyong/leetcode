// 572. Subtree of Another Tree

package main

import (
	"bufio"
	"fmt"
	"leetcode/structs"
	"leetcode/utils"
	"os"

	"github.com/samber/lo"
)

func isSameTree(left *structs.TreeNode, right *structs.TreeNode) bool {
	if left == nil && right == nil {
		return true
	}
	if left == nil || right == nil || left.Val != right.Val {
		return false
	}
	return isSameTree(left.Left, right.Left) && isSameTree(left.Right, right.Right)
}

func isSubtree(root *structs.TreeNode, subRoot *structs.TreeNode) bool {
	if root == nil {
		return false
	}
	if root.Val == subRoot.Val && isSameTree(root, subRoot) {
		return true
	}
	return isSubtree(root.Left, subRoot) || isSubtree(root.Right, subRoot)
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	var lines []string
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	const testSize int = 2

	for _, test := range lo.Chunk(lines, testSize) {
		root := utils.ToTree(test[0])
		subRoot := utils.ToTree(test[1])
		result := isSubtree(root, subRoot)
		fmt.Println(result)
	}
}
