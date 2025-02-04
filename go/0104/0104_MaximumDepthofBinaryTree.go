// 104. Maximum Depth of Binary Tree

package main

import (
	"bufio"
	"fmt"
	"leetcode/structs"
	"leetcode/utils"
	"os"

	"github.com/samber/lo"
)

func maxDepth(root *structs.TreeNode) int {
	if root == nil {
		return 0
	}
	left := maxDepth(root.Left) + 1
	right := maxDepth(root.Right) + 1
	return max(left, right)
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
		result := maxDepth(root)
		fmt.Println(result)
	}
}
