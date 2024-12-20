// 2415. Reverse Odd Levels of Binary Tree

package main

import (
	"bufio"
	"leetcode/structs"
	"leetcode/utils"
	"os"

	"github.com/samber/lo"
)

func dfsSwap(left *structs.TreeNode, right *structs.TreeNode, odd bool) {
	if left == nil { // no need to check right since perfect binary tree
		return
	}
	if odd {
		left.Val, right.Val = right.Val, left.Val
	}
	dfsSwap(left.Left, right.Right, !odd)
	dfsSwap(left.Right, right.Left, !odd)
}

func reverseOddLevels(root *structs.TreeNode) *structs.TreeNode {
	dfsSwap(root.Left, root.Right, true)
	return root
}

// bfs
// func reverseOddLevels(root *structs.TreeNode) *structs.TreeNode {
// 	queue := []*structs.TreeNode{root}
// 	isOddLevel := false

// 	for len(queue) > 0 {
// 		levelSize := len(queue)

// 		if isOddLevel {
// 			for i := range levelSize / 2 {
// 				temp := queue[i].Val
// 				queue[i].Val = queue[levelSize-1-i].Val
// 				queue[levelSize-1-i].Val = temp
// 			}
// 		}

// 		for i := range levelSize {
// 			curr := queue[i]
// 			if curr.Left != nil { // no need to check right since perfect binary tree
// 				queue = append(queue, curr.Left, curr.Right)
// 			}
// 		}

// 		queue = queue[levelSize:]
// 		isOddLevel = !isOddLevel
// 	}

// 	return root
// }

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	var lines []string
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	const testSize int = 1

	for _, test := range lo.Chunk(lines, testSize) {
		root := utils.ToTree(test[0])
		result := reverseOddLevels(root)
		utils.PrintTreeInOrder(result)
	}
}
