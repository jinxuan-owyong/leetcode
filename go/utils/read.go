package utils

import (
	"bufio"
)

func ReadInt(scanner *bufio.Scanner) int {
	if !scanner.Scan() {
		panic("Failed to read input")
	}
	line := scanner.Text()
	return ParseInt(line)
}

func ReadString(scanner *bufio.Scanner) string {
	if !scanner.Scan() {
		panic("Failed to read input")
	}
	line := scanner.Text()
	return line[1 : len(line)-1]
}
