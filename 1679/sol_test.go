package main

import "testing"

func TestMaxOpe(t *testing.T) {
	test_nums := []int{1, 2, 3, 4}
	test_k := 5
	expect := 2

	actual := maxOperations(test_nums, test_k)

	if actual != expect {
		t.Error("actual:", actual, "expect:", expect)
	}
}
