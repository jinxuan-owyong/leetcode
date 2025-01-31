package utils

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func PrintLinkedList(head *ListNode) {
	curr := head
	for curr != nil {
		fmt.Print(curr.Val, " ")
		curr = curr.Next
	}
	fmt.Println()
}

func ToLinkedList(nums []int) *ListNode {
	var prev *ListNode = nil
	for i := len(nums) - 1; i >= 0; i -= 1 {
		prev = &ListNode{nums[i], prev}
	}
	return prev
}
