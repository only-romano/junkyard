package boobs

import (
	"fmt"
	"strconv"
)

func Step2() {
	printNums()
	errShortInput = strconv.ErrRange

	var mass = []int{2, 4, 8, 16, 32, 64, 128, 256}
	runNumsCycle(mass, 8, 256, 1, false)
	runNumsCycle([]int{256}, 32, 512, 7, false)
	runNumsCycle(mass, 32, 128, 1, true)

	printNums()
}

var (
	errShortInput error
	nums          []int
)

func runNumsCycle(src []int, check1, check2, step int, validateOnly bool) {
Loop:
	for n := 0; n < len(src); n += step {
		switch {
		case src[n] < check1:
			if validateOnly {
				break
			}
			step = 1
			go updateNums(src[n])
		case src[n] < check2:
			if n+1 >= len(src) {
				fmt.Println("occurred error in Nums array:", errShortInput)
				break Loop
			}
			if validateOnly {
				break
			}
			step = 2
			go updateNums(src[n] + src[n+1]<<2)
		}
	}
}

func printNums() {
	var str string;
	if len(nums) == 0 {
		str = "Step 2 starts here, empty Nums array:"
	} else {
		str = "Step 2 ends here, updated Nums array:"
	}

	fmt.Println(str, nums)
}

func updateNums(num int) {
	fmt.Println("updating Nums array with", num)
	nums = append(nums, num)
}
