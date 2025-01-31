// 21. Merge Two Sorted Lists

package main

import (
	"bufio"
	"encoding/json"
	"leetcode/utils"
	"os"

	"github.com/samber/lo"
)

func mergeTwoLists(list1 *utils.ListNode, list2 *utils.ListNode) *utils.ListNode {
	if list1 == nil && list2 == nil {
		return nil
	} else if list1 != nil && list2 == nil {
		return list1
	} else if list1 == nil && list2 != nil {
		return list2
	}

	var result *utils.ListNode = nil
	var curr *utils.ListNode = nil
	if list1.Val < list2.Val {
		result = list1
		curr = list1
		list1 = list1.Next
	} else {
		result = list2
		curr = list2
		list2 = list2.Next
	}

	// compare and take the smallest element
	for list1 != nil && list2 != nil {
		if list1.Val < list2.Val {
			curr.Next = list1
			list1 = list1.Next
		} else {
			curr.Next = list2
			list2 = list2.Next
		}
		curr = curr.Next
	}

	// attach leftover elements to result
	if list1 != nil {
		curr.Next = list1
	}

	if list2 != nil {
		curr.Next = list2
	}

	return result
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	var lines []string
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	const testSize int = 2

	for _, test := range lo.Chunk(lines, testSize) {
		var first []int
		var second []int
		if err1 := json.Unmarshal([]byte(test[0]), &first); err1 != nil {
			panic(err1)
		}
		if err2 := json.Unmarshal([]byte(test[1]), &second); err2 != nil {
			panic(err2)
		}
		result := mergeTwoLists(utils.ToLinkedList(first), utils.ToLinkedList(second))
		utils.PrintLinkedList(result)
	}
}
