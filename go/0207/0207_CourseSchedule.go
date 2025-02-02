// 207. Course Schedule

package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"os"
	"strconv"

	"github.com/samber/lo"
)

func canFinish(numCourses int, prerequisites [][]int) bool {
	// we can perform dfs to see how many courses we can achieve from the starting courses
	var adjList = make([][]int, numCourses)
	for i := range numCourses {
		adjList[i] = []int{}
	}

	// inDegree is also the number of prerequisite courses of "want"
	var inDegree = make([]int, numCourses)
	for _, p := range prerequisites {
		want, need := p[0], p[1]
		adjList[need] = append(adjList[need], want)
		inDegree[want] += 1
	}

	queue := []int{}
	for start, in := range inDegree {
		if in == 0 {
			queue = append(queue, start)
		}
	}

	count := 0
	for len(queue) > 0 {
		curr := queue[0]
		queue = queue[1:]
		count += 1

		// kahn's algorithm: explore node only if all prerequisites are fulfilled
		for _, unlocked := range adjList[curr] {
			inDegree[unlocked] -= 1
			if inDegree[unlocked] == 0 {
				queue = append(queue, unlocked)
			}
		}
	}

	return count == numCourses
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	var lines []string
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	const testSize int = 2

	for _, test := range lo.Chunk(lines, testSize) {
		var prerequisites [][]int
		numCourses, _ := strconv.Atoi(test[0])
		json.Unmarshal([]byte(test[1]), &prerequisites)
		result := canFinish(numCourses, prerequisites)
		fmt.Println(result)
	}
}
