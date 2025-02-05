// 235. Lowest Common Ancestor of a Binary Search Tree

package main

import (
	"bufio"
	"fmt"
	"leetcode/structs"
	"leetcode/utils"
	"os"

	"github.com/samber/lo"
)

func lowestCommonAncestor(root, p, q *structs.TreeNode) *structs.TreeNode {
	// the lowest common ancestor is the lowest subtree that contains both p and q
	// BST property: elements in left subtree < root.Val < elements in right subtree
	// since p and q are guaranteed to be in the tree, perform DFS until we reach a root where p and q are on different sides
	// keep track of depth to find the deepest common node
	if root == nil {
		return nil // should never reach here
	}
	if p.Val < root.Val && q.Val < root.Val {
		return lowestCommonAncestor(root.Left, p, q)
	}
	if p.Val > root.Val && q.Val > root.Val {
		return lowestCommonAncestor(root.Right, p, q)
	}
	// p and q must either be on different sides or one of them is the root
	return root
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	var lines []string
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	const testSize int = 3

	for _, test := range lo.Chunk(lines, testSize) {
		root := utils.ToTree(test[0])
		p := &structs.TreeNode{Val: utils.ParseInt(test[1])}
		q := &structs.TreeNode{Val: utils.ParseInt(test[2])}
		result := lowestCommonAncestor(root, p, q)
		fmt.Println(result.Val)
	}
}
