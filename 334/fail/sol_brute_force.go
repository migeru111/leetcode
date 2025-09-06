package main

func increasingTriplet(nums []int) bool {

	for i := range nums {
		for j := range nums {
			for k := range nums {
				//fmt.Println(i,j,k,nums[i],nums[j],nums[k])
				if i < j && j < k {
					if nums[i] < nums[j] && nums[j] < nums[k] {
						return true
					}
				}
			}
		}
	}
	return false
}
