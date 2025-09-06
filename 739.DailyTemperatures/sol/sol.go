package sol

func dailyTemperatures(temperatures []int) []int {
	len_temp := len(temperatures)
	res := make([]int, len_temp)

	//擬似スタック作る時には、要素数０で作ればいい
	stack := make([]int, 0)

	for i := range temperatures {
		for len(stack) > 0 && temperatures[i] > temperatures[stack[len(stack)-1]] {
			end := stack[len(stack)-1]
			//末尾から要素削除
			stack = stack[:len(stack)-1]
			res[end] = i - end
		}

		stack = append(stack, i)

	}
	return res
}
