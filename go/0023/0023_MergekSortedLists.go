// 23. Merge k Sorted Lists

package main

import (
	"bufio"
	"encoding/json"
	"leetcode/utils"
	"os"

	"github.com/emirpasic/gods/trees/binaryheap"
	"github.com/samber/lo"
)

func mergeKLists(lists []*utils.ListNode) *utils.ListNode {
	pq := binaryheap.NewWith(func(_a, _b interface{}) int {
		a, b := _a.(*utils.ListNode), _b.(*utils.ListNode)
		return a.Val - b.Val
	})

	// populate first level of nodes and skip empty lists
	for _, list := range lists {
		if list != nil {
			pq.Push(list)
		}
	}

	if pq.Size() == 0 {
		return nil
	}

	// at least 1 list in pq
	head, _ := pq.Pop()
	curr := head.(*utils.ListNode)
	if curr.Next != nil {
		pq.Push(curr.Next)
	}

	for !pq.Empty() {
		_top, _ := pq.Pop()
		// get the smallest node among k candidates
		top := _top.(*utils.ListNode)
		curr.Next = top
		curr = curr.Next
		if top.Next != nil {
			pq.Push(top.Next)
		}
	}

	return head.(*utils.ListNode)
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	var lines []string
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	const testSize int = 1

	for _, test := range lo.Chunk(lines, testSize) {
		var nums [][]int
		json.Unmarshal([]byte(test[0]), &nums)
		lists := lo.Map(nums, func(arr []int, _ int) *utils.ListNode {
			return utils.ToLinkedList(arr)
		})
		result := mergeKLists(lists)
		utils.PrintLinkedList(result)
	}
}
