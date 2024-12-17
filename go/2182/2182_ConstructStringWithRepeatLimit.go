// 2182. Construct String With Repeat Limit

package main

import (
	"bufio"
	"fmt"
	"leetcode/utils"
	"os"
	"strings"

	"github.com/emirpasic/gods/trees/binaryheap"
	"github.com/samber/lo"
)

type Char struct {
	id    rune
	count int
}

func repeatLimitedString(s string, repeatLimit int) string {
	pq := binaryheap.NewWith(func(_a, _b interface{}) int {
		a, b := _a.(Char), _b.(Char)
		if a.id == b.id {
			return b.count - a.count // max-heap
		}
		return int(b.id) - int(a.id) // lexicographically largest
	})

	freq := make(map[rune]int)
	for _, c := range s {
		freq[c] += 1
	}

	for k, v := range freq {
		pq.Push(Char{id: k, count: v})
	}

	var result strings.Builder
	prev := rune(0)
	// greedily take the next largest character in lexicographic order
	for !pq.Empty() {
		_curr, _ := pq.Pop()
		curr := _curr.(Char)

		// no more characters to append, remaining will result in repeatLimit exceeding
		if curr.id == prev {
			break
		}

		for range min(curr.count, repeatLimit) {
			result.WriteRune(curr.id)
		}
		prev = curr.id

		// add next character to prevent exceeding repeatLimit if curr is still the next largest
		if pq.Size() > 0 && curr.count > repeatLimit {
			_next, _ := pq.Pop()
			next := _next.(Char)
			result.WriteRune(next.id)
			next.count -= 1
			if next.count > 0 {
				pq.Push(next)
			}
			prev = next.id
		}

		curr.count -= min(curr.count, repeatLimit)
		if curr.count > 0 {
			pq.Push(curr)
		}
	}

	return result.String()
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	var lines []string
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	const testSize int = 2

	for _, test := range lo.Chunk(lines, testSize) {
		s := test[0]
		s = s[1 : len(s)-1]
		repeatLimit := utils.ParseInt(test[1])
		result := repeatLimitedString(s, repeatLimit)
		fmt.Println(result)
	}
}
