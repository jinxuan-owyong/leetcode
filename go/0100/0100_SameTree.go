// 100. Same Tree

package main

import (
	"bufio"
	"fmt"
	"leetcode/structs"
	"leetcode/utils"
	"os"

	"github.com/samber/lo"
)

func isSameTree(p *structs.TreeNode, q *structs.TreeNode) bool {
	if p == nil && q == nil {
		return true
	}
	if p == nil || q == nil || p.Val != q.Val {
		return false
	}
	return isSameTree(p.Left, q.Left) && isSameTree(p.Right, q.Right)
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	var lines []string
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	const testSize int = 2

	for _, test := range lo.Chunk(lines, testSize) {
		p := utils.ToTree(test[0])
		q := utils.ToTree(test[1])
		result := isSameTree(p, q)
		fmt.Println(result)
	}
}
