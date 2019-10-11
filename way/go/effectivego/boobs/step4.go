package boobs

import (
	"bytes"
	"fmt"
	"sync"
)

func StartTrace() {
	defer untraceIt(traceIt("b"))
	fmt.Println("in b")
	a()
}

func traceIt(s string) string {
	fmt.Println("entering", s)
	return s
}

func untraceIt(s string) {
	fmt.Println("leaving", s)
}

func a() {
	defer untraceIt(traceIt("a"))
	fmt.Println("in a")
}

type SyncedBuffer struct {
	lock sync.Mutex
	buffer bytes.Buffer
}
