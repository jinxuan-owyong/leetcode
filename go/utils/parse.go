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
