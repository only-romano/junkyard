package boobs

import (
	"fmt"
	"sync"
	"time"
)

func Step3() {
	a := 2+3 * 4
	fmt.Println(a)

	newMap = make(map[string] int)
	for a > 0 {
		go count()
		go createMap()
		a--
	}

	fmt.Println(oldMap)
	time.Sleep(50)
	fmt.Println(oldMap)
	fmt.Println()
}

var (
	countLock sync.Mutex
	inputCount uint32
	newMap map[string] int
)

var oldMap = map[int] string {
	1: "cool",
	2: "fuck",
	3: "fat",
	4: "girl",
	5: "shit",
	6: "me",
}

func count() {
	for i := 0; i < 10; i++ {
		countLock.Lock()
		inputCount += uint32(i)
		countLock.Unlock()
	}
}

func createMap() {
	for key, value := range oldMap {
		countLock.Lock()
		newMap[value] = key
		countLock.Unlock()
	}

	for key := range oldMap {
		if key < 3 {
			delete(oldMap, key)
		}
	}
}
