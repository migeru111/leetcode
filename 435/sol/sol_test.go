package main

import "testing"

func TestCase001(t *testing.T) {
	testdata := [][]int{
		{1, 2},
		{2, 3},
		{3, 4},
		{1, 2},
	}
	expected := 1
	actual := eraseOverlapIntervals(testdata)

	if expected != actual {
		t.Error("expected:", expected, "is different from actual:", actual)
	}

}
