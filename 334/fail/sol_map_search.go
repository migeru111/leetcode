package main

func increasingTriplet(nums []int) bool {

	//keyがnumsの値、valueがnumsのindexのマップを作成
	m := make(map[int][]int)
	for i, v := range nums {
		if _, ok := m[v]; ok {
			m[v] = append(m[v], i)
		} else {
			m[v] = make([]int, 0)
			m[v] = append(m[v], i)
		}
	}
	//fmt.Println(m)

	for i := range m {
		for j := range m {
			for k := range m {
				if i < j && j < k {
					for _, v_s := range m[i] {
						for _, v_t := range m[j] {
							for _, v_u := range m[k] {
								//fmt.Println(i,j,k,v_s,v_t,v_u)
								if v_s < v_t && v_t < v_u {
									return true
								}
							}
						}
					}
				}
			}
		}
	}
	return false
}
