package dailytemperatures

import (
	"slices"
	"testing"
)

func TestDailyTemperatures(t *testing.T) {
	testdata01 := []int{73, 74, 75, 71, 69, 72, 76, 73}
	answer01 := []int{1, 1, 4, 2, 1, 1, 0, 0}

	actual := dailyTemperatures(testdata01)
	if slices.Compare(actual, answer01) != 0 {
		t.Error("testdata01 failed.actual:", actual, "answer:", answer01)
	}

}
