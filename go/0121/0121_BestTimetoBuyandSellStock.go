// 121. Best Time to Buy and Sell Stock

package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"os"

	"github.com/samber/lo"
)

func maxProfit(prices []int) int {
	/*
		we can achieve the highest profit with the lowest price, so we should keep track of this value as we iterate
		using the lowest price, then we can determine if selling at the current iteration fetches a better price
	*/
	result := 0
	lowest := prices[0]
	for _, curr := range prices {
		lowest = min(lowest, curr)
		result = max(result, curr-lowest)
	}
	return result
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
		result := maxProfit(prices)
		fmt.Println(result)
	}
}
