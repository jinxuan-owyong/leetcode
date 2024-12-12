// 2558. Take Gifts From the Richest Pile

package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"leetcode/utils"
	"math"
	"os"

	"github.com/emirpasic/gods/trees/binaryheap"
	"github.com/samber/lo"
)

const testSize int = 2

func pickGifts(gifts []int, k int) int64 {
	pq := binaryheap.NewWithIntComparator()
	for _, g := range gifts {
		pq.Push(-g)
	}

	for range k {
		_t, ok := pq.Pop()
		if !ok || _t.(int) == 0 {
			break
		}
		top := -_t.(int)
		leave := int(math.Floor(math.Sqrt(float64(top))))
		pq.Push(-leave)
	}

	remaining := int64(0)
	for !pq.Empty() {
		t, _ := pq.Pop()
		remaining += int64(-t.(int))
	}

	return remaining
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	var lines []string
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	for _, test := range lo.Chunk(lines, testSize) {
		var gifts []int
		err := json.Unmarshal([]byte(test[0]), &gifts)
		if err != nil {
			panic(err)
		}
		k := utils.ParseInt(test[1])
		result := pickGifts(gifts, k)
		fmt.Println(result)
	}
}
