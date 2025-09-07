package main

func maxOperations(nums []int, k int) int {
	m := make(map[int]int)
	res := 0
	travarsed := make(map[int]bool)

	for _, v := range nums {
		if _, ok := m[v]; ok {
			m[v] += 1
		} else {
			m[v] = 1
		}
	}

	//fmt.Println(m)

	for key := range m {
		if !(travarsed[key] || travarsed[k-key]) {
			if _, ok := m[key]; ok {
				if _, ok2 := m[k-key]; ok2 {
					//fmt.Println(k, key, m[key], m[k-key])
					if key == k-key {
						res += m[key] / 2
					} else {
						res += min(m[key], m[k-key])
					}
				}
			}
		}
		travarsed[key] = true
		//fmt.Println(res,travarsed)
	}
	return res
}
