// 226. Invert Binary Tree

package main

import (
	"bufio"
	"leetcode/structs"
	"leetcode/utils"
	"os"

	"github.com/samber/lo"
)

func invertTree(root *structs.TreeNode) *structs.TreeNode {
	if root != nil {
		root.Left, root.Right = root.Right, root.Left
		invertTree(root.Left)
		invertTree(root.Right)
	}
	return root
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
		result := invertTree(root)
		utils.PrintTreeInOrder(result)
	}
}
