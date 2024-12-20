package utils

import (
	"encoding/json"
	"fmt"
	"leetcode/structs"
	"slices"

	"github.com/samber/lo"
)

func ToTree(arr string) *structs.TreeNode {
	if arr == "[]" {
		return nil
	}

	var nums []*int
	if err := json.Unmarshal([]byte(arr), &nums); err != nil {
		panic(err)
	}

	nodes := lo.Map(nums, func(node *int, _ int) *structs.TreeNode {
		if node == nil {
			return nil
		}
		temp := structs.TreeNode{Val: *node}
		return &temp
	})

	kids := slices.Clone(nodes)
	slices.Reverse(kids)
	root := kids[len(kids)-1]
	kids = kids[:len(kids)-1]

	for _, node := range nodes {
		if node != nil {
			if len(kids) > 0 {
				node.Left = kids[len(kids)-1]
				kids = kids[:len(kids)-1]
			}
			if len(kids) > 0 {
				node.Right = kids[len(kids)-1]
				kids = kids[:len(kids)-1]
			}
		}
	}

	return root
}

func printTreeInOrder(root *structs.TreeNode) {
	if root == nil {
		return
	}
	printTreeInOrder(root.Left)
	fmt.Print(root.Val, " ")
	printTreeInOrder(root.Right)
}

func PrintTreeInOrder(root *structs.TreeNode) {
	printTreeInOrder(root)
	fmt.Println()
}
