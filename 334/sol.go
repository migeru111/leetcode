package main

import (
	"math"
)

func increasingTriplet(nums []int) bool {
	low := math.MaxInt64
	mid := math.MaxInt64

	for _, v := range nums {
		if v < low {
			low = v
		} else if v > low && mid > v {
			mid = v
		} else if v > mid {
			return true
		}
	}
	return false

}
