package boobs

/*
import (
	"fmt"
	"strings"
	"sync"
	"time"
)

type T struct {
	name  string
	value int
}

func Step0() {

	for pos, char := range "日本\x80語" {
		fmt.Printf("character %#U starts at byte position %d\n", char, pos)
	}

	var word = []string {"s", "e", "x", "e"}
	// Reverse a
	for i, j := 0, len(word)-1; i < j; i, j = i+1, j-1 {
		word[i], word[j] = word[j], word[i]
	}

	fmt.Println(strings.Join(word, ""), unhex('9'), shouldEscape('?'))


	for i := 0; i < 5; i++ {
		defer fmt.Printf("%d", i)
	}


	var bytes1 = []byte {'1', 'A', 'C'}
	var bytes2 = []byte {'1', '2', '3', '4'}

	for i := 0; i < len(bytes2); {
		var x int
		x, i = boobs.NextInt(bytes2, i)
		fmt.Println(x, i)
	}

	switch boobs.Compare(bytes1, bytes2) {
	case 0:
		fmt.Print("slice of bytes a == slice of bytes b")
	case 1:
		fmt.Print("slice of bytes a > slice of bytes b")
	case -1:
		fmt.Print("slice of bytes a < slice of bytes b")
	}

	fmt.Println()
}
*/