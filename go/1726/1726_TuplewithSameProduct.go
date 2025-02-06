// 1726. Tuple with Same Product

package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"os"

	"github.com/samber/lo"
)

func tupleSameProduct(nums []int) int {
	if len(nums) < 4 {
		return 0
	}
	/*
		For every 4 integers fulfilling a*b=c*d, there are 8 combinations
		instead of searching for all tuples, count number of pairs that give us the same product
		if there are 2 or more unique pairs, then a*b=c*d is true
	*/
	pairs := make(map[int]int)
	for i := range nums {
		for j := range nums {
			if i < j {
				pairs[nums[i]*nums[j]] += 1
			}
		}
	}

	count := 0
	for _, curr := range pairs {
		if curr >= 2 {
			// if there are n pairs, then the number of possible tuples is nC2
			// nCr = n! / (r! * (n-r)!)
			// nC2 = n! / (2 * (n-2)!)
			//     = 0.5 * n * (n-1)
			count += curr * (curr - 1) / 2
		}
	}
	return count * 8
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
		result := tupleSameProduct(nums)
		fmt.Println(result)
	}
}
