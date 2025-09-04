package main

import (
	"fmt"
	"slices"
)

func eraseOverlapIntervals(intervals [][]int) int {
	/* a := [][]int{
		{1, 2},
		{2, 3},
		{3, 4},
		{1, 3},
	} */
	fmt.Println("before", intervals)
	slices.SortFunc(intervals, func(a, b []int) int {
		if a[0] < b[0] {
			return -1
		} else if a[0] > b[0] {
			return 1
		} else {
			return 0
		}
	})
	fmt.Println("after", intervals)

	bf_end := intervals[0][1]
	res := 0

	for _, v := range intervals[1:] {
		if v[0] < bf_end {
			res += 1
			bf_end = min(bf_end, v[1])
		} else {
			bf_end = v[1]
		}
	}

	fmt.Println(res)
	return res

}

func main() {
	//res:=eraseOverlapIntervals()
}
