package utils

import (
	"strconv"
	"strings"

	"github.com/samber/lo"
)

func ParseInt(s string) int {
	num, err := strconv.Atoi(s)
	if err != nil {
		panic(err)
	}
	return num
}

func ParseArrInt(s string, delim string) []int {
	arr := strings.Split(s, delim)
	return lo.Map(arr, func(num string, _ int) int {
		return ParseInt(num)
	})
}

func ToByteArray(row []string) []byte {
	return lo.Map(row, func(s string, _ int) byte {
		return s[0]
	})
}

func To2DByteArray(data [][]string) [][]byte {
	return lo.Map(data, func(row []string, _ int) []byte {
		return ToByteArray(row)
	})
}
