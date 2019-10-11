package boobs

import (
	"bufio"
	"effectivego/helpers"
	"fmt"
	"io"
	"os"
)

var t interface{}

func SexyInt() {
	t = chooseFunc()
	switch t := t.(type) {
	case bool:
		fmt.Printf("boolean %t\n", t)
	case int:
		fmt.Printf("integer %d\n", t)
	case *bool:
		fmt.Printf("pointer to boolean %t\n", *t)
	case *int:
		fmt.Printf("pointer to integer %d\n", *t)
	default:
		fmt.Printf("unexpected type %T\n %s", t, t)
	}
}

func chooseFunc() interface{} {
	randFunc := helpers.GetRandomInt(5)
	switch randFunc {
	case 0:
		return interfaceBool()
	case 1:
		return interfaceInt()
	case 2:
		return interfaceBoolPoint()
	case 3:
		return interfaceIntPoint()
	default:
		return interfaceString()
	}
}

func interfaceBool() bool {
	pool := helpers.GetRandomInt(2)
	return pool == 1
}

func interfaceBoolPoint() *bool {
	pool := helpers.GetRandomInt(2) == 1
	return &pool
}

func interfaceInt() int {
	return helpers.GetRandomInt(10)
}

func interfaceIntPoint() *int {
	a := helpers.GetRandomInt(10)
	return &a
}

func interfaceString() string {
	return "Hello!\n"
}

func ReadFull(r bufio.Reader, buf []byte) (n int, err error) {
	for len(buf) > 0 && err != nil {
		var nr int
		nr, err = r.Read(buf)
		n += nr
		buf = buf[nr:]
	}
	return
}

func Contents(filename string) (string, error) {
	f, err := os.Open(filename)
	if err != nil {
		return "", err
	}
	defer f.Close()

	var result []byte
	buf := make([]byte, 100)
	for {
		n, err := f.Read(buf[0:])
		result = append(result, buf[0:n]...)
		if err != nil {
			if err == io.EOF {
				break
			}
			return "", err
		}
	}

	return string(result), nil
}

func trace(s string) {
	fmt.Println("entering:", s)

}

func untrace(s string) {
	fmt.Println("leaving:", s)
}

func A() {
	trace ("a")
	defer untrace("a")
	fmt.Println("Nandacoco")
}
