// 3151. Special Array I

package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"os"

	"github.com/samber/lo"
)

func isArraySpecial(nums []int) bool {
	// both same parity will sum to either 0 or 2
	// different parity yields (0, 1) or (1, 0), so total = 1
	for i := 0; i < len(nums)-1; i += 1 {
		if nums[i]%2+nums[i+1]%2 != 1 {
			return false
		}
	}
	return true
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	var lines []string
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	const testSize int = 1

	for _, test := range lo.Chunk(lines, testSize) {
		var nums []int
		json.Unmarshal([]byte(test[0]), &nums)
		result := isArraySpecial(nums)
		fmt.Println(result)
	}
}
