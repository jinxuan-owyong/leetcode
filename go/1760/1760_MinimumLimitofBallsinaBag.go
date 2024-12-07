// 1760. Minimum Limit of Balls in a Bag

package main

import (
	"bufio"
	"fmt"
	"leetcode/utils"
	"math"
	"os"
	"slices"
)

func minimumSize(nums []int, maxOperations int) int {
	i, j := 1, slices.Max(nums)

	for i <= j {
		bagSize := float64(i + (j-i)/2)

		// determine how many bags result from the current bag size
		// resulting bag count corresponds to the number of operations + initial bag count
		count := 0
		for _, num := range nums {
			count += int(math.Ceil(float64(num) / bagSize))
		}

		numOperations := count - len(nums)
		if numOperations > maxOperations {
			i = int(bagSize) + 1
		} else {
			j = int(bagSize) - 1
		}
	}

	return i
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	n := utils.ReadInt(scanner)
	for range n {
		nums := utils.ParseArrInt(utils.ReadString(scanner), ",")
		maxOperations := utils.ReadInt(scanner)
		result := minimumSize(nums, maxOperations)
		fmt.Println(result)
	}
}
