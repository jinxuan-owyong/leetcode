package utils

import (
	"bufio"
	"strconv"
)

func ReadInt(scanner *bufio.Scanner) int {
	if !scanner.Scan() {
		panic("Failed to read input")
	}
	line := scanner.Text()
	num, err := strconv.Atoi(line)
	if err != nil {
		panic(err)
	}
	return num
}

func ReadString(scanner *bufio.Scanner, stripQuotes bool) string {
	if !scanner.Scan() {
		panic("Failed to read input")
	}
	line := scanner.Text()
	if stripQuotes {
		return line[1 : len(line)-1]
	}
	return line
}
