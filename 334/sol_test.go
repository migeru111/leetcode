package main

import "testing"

func TestIncreaseTriplet(t *testing.T) {
	testdata := []int{1, 2, 3, 4, 5}
	except := true
	actual := increasingTriplet(testdata)

	if except != actual {
		t.Error(actual, except)
	}
}
