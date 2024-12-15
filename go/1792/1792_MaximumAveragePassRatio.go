// 1792. Maximum Average Pass Ratio

package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"leetcode/utils"
	"os"

	"github.com/emirpasic/gods/trees/binaryheap"
	"github.com/samber/lo"
)

func frac(x, y int) float64 {
	return float64(x) / float64(y)
}

func maxAverageRatio(classes [][]int, extraStudents int) float64 {
	pq := binaryheap.NewWith(func(_a, _b interface{}) int {
		a, b := _a.([]int), _b.([]int)
		// order by highest increase in ratio (max heap)
		changeA := frac(a[0]+1, a[1]+1) - frac(a[0], a[1])
		changeB := frac(b[0]+1, b[1]+1) - frac(b[0], b[1])
		if changeA < changeB {
			return 1
		}
		return -1
	})

	for _, class := range classes {
		pq.Push(class)
	}

	// greedily assign extra students to the class with lowest pass rate
	for range extraStudents {
		_curr, _ := pq.Pop()
		curr := _curr.([]int)
		pq.Push([]int{curr[0] + 1, curr[1] + 1})
	}

	// calculate average
	result := float64(0)
	n := float64(0)
	for !pq.Empty() {
		_curr, _ := pq.Pop()
		curr := _curr.([]int)
		result += float64(curr[0]) / float64(curr[1])
		n += 1
	}

	return result / n
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	var lines []string
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	const testSize int = 2

	for _, test := range lo.Chunk(lines, testSize) {
		var classes [][]int
		if err := json.Unmarshal([]byte(test[0]), &classes); err != nil {
			panic(err)
		}
		extraStudents := utils.ParseInt(test[1])
		result := maxAverageRatio(classes, extraStudents)
		fmt.Println(result)
	}
}
