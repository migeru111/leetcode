package dailytemperatures

import (
	"fmt"
	"slices"
)

func dailyTemperatures(temperatures []int) []int {

	// answerの初期化
	answer := make([]int, len(temperatures))
	fmt.Println(answer)

	// new_tempの作成
	new_temp := make([][]int, len(temperatures))
	for index := range new_temp {
		new_temp[index] = []int{index, temperatures[index]}
	}
	fmt.Println(new_temp)

	//new_tempを安定ソート
	slices.SortStableFunc(new_temp, func(a, b []int) int {
		if a[1] < b[1] {
			return -1
		} else if a[1] > b[1] {
			return 1
		} else {
			return 0
		}
	})

	fmt.Println(new_temp)

	for i, v := range new_temp {
		for _, w := range new_temp[i+1:] {
			if w[1] > v[1] && w[0] > v[0] {
				//println(i, v, w)
				answer[v[0]] = w[0] - v[0]
				break
			}
		}
	}

	fmt.Println(answer)

	return answer
}
