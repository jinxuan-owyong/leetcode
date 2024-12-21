// 2872. Maximum Number of K-Divisible Components

package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"leetcode/utils"
	"os"

	"github.com/samber/lo"
)

func dfs(i int, parent int, k int, adjList map[int][]int, values []int, result *int) int {
	// if parent has >= 2 children (not necessarily binary tree as well), and parent + 1
	// child = m * k, the other child cannot be "abandoned" -> add until multiple of k

	// use itself as the root of the subtree
	// if we find a divisible component, then it should add to the result
	count := values[i]
	for _, nei := range adjList[i] { // if leaf node, then this will not run
		if nei != parent {
			count += dfs(nei, i, k, adjList, values, result)
		}
	}

	// "remove" the edge when sum of values in component is multiple of k, including leaf
	if count%k == 0 {
		*result += 1
		return 0
	}

	return count
}

func maxKDivisibleComponents(n int, edges [][]int, values []int, k int) int {
	// if a leaf node is k-divisible, then it is a component on its own
	// otherwise it must be connected to its parent
	adjList := make(map[int][]int)
	for _, edge := range edges {
		u, v := edge[0], edge[1]
		adjList[u] = append(adjList[u], v)
		adjList[v] = append(adjList[v], u)
	}

	result := 0
	dfs(0, -1, k, adjList, values, &result)
	return result
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	var lines []string
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	const testSize int = 4

	for _, test := range lo.Chunk(lines, testSize) {
		n := utils.ParseInt(test[0])
		k := utils.ParseInt(test[3])

		var edges [][]int
		if err := json.Unmarshal([]byte(test[1]), &edges); err != nil {
			panic(err)
		}
		var values []int
		if err := json.Unmarshal([]byte(test[2]), &values); err != nil {
			panic(err)
		}
		fmt.Println(edges)
		result := maxKDivisibleComponents(n, edges, values, k)
		fmt.Println(result)
	}
}
