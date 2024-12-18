// 1475. Final Prices With a Special Discount in a Shop

package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"os"

	"github.com/samber/lo"
)

func finalPrices(prices []int) []int {
	for i, original := range prices {
		for _, discount := range prices[i+1:] { // j > i, O(1) slicing due to pointer nature of slices
			if discount <= original { // prices[j] <= prices[i]
				prices[i] = min(prices[i], original-discount)
				break // minimum index
			}
		}
	}
	return prices
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	var lines []string
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	const testSize int = 1

	for _, test := range lo.Chunk(lines, testSize) {
		var prices []int
		if err := json.Unmarshal([]byte(test[0]), &prices); err != nil {
			panic(err)
		}
		result := finalPrices(prices)
		fmt.Println(result)
	}
}
