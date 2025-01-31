// 19. Remove Nth Node From End of List

package main

import (
	"bufio"
	"encoding/json"
	"leetcode/utils"
	"os"

	"github.com/samber/lo"
)

func removeNthFromEnd(head *utils.ListNode, n int) *utils.ListNode {
	// trivial: get size of linked list, then traverse size-n times to locate the target node
	// two pointers: offset right pointer by n, then move left and right together until right hits the end
	// if we only use left, then we need to keep track of the previous of left as well, so use leftPrev instead
	leftPrev := &utils.ListNode{Val: 0, Next: head}
	right := head

	for range n {
		right = right.Next
	}

	// special case: n == len(head)
	if right == nil {
		return head.Next
	}

	for right != nil {
		leftPrev = leftPrev.Next
		right = right.Next
	}

	// remove Nth from end
	leftPrev.Next = leftPrev.Next.Next
	return head
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	var lines []string
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	const testSize int = 2

	for _, test := range lo.Chunk(lines, testSize) {
		var arr []int
		json.Unmarshal([]byte(test[0]), &arr)
		n := utils.ParseInt(test[1])
		result := removeNthFromEnd(utils.ToLinkedList(arr), n)
		utils.PrintLinkedList(result)
	}
}
