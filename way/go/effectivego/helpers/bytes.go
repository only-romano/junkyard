package helpers

func Compare(a, b []byte) int {
	for i := 0; i < len(a) && i < len(b); i++ {
		switch {
		case a[i] > b[i]:
			return 1
		case a[i] < b[i]:
			return -1
		}
	}

	switch {
	case len(a) > len(b):
		return 1
	case len(a) < len(b):
		return -1
	}

	return 0
}

func NextInt(b []byte, i int) (int, int) {
	for ; i < len(b) && !isDigit(b[i]); i++ {
	}

	x := 0

	for ; i < len(b) && isDigit(b[i]); i++ {
		x = x*10 + int(b[i]) - '0'
	}

	return x, i
}

func ShouldEscape(c byte) bool {
	switch c {
	case ' ', '?', '&', '=', '#', '+', '%':
		return true
	}
	return false
}

func Unhex(c byte) byte {
	switch {
	case '0' <= c && c <= '9':
		return c - '0'
	case 'a' <= c && c <= 'f':
		return c - 'a' + 10
	case 'A' <= c && c <= 'F':
		return c - 'A' + 10
	}

	return 0
}


func isDigit(b byte) bool {
	return b >= '0' && b <= '9'
}
