letters = {
	"a": ["    A    ", "   A A   ", "  A   A  ", " A A A A ", "A       A"],
	"b": ["B B B B  ", "B      B ", "B B B B B", "B       B", "B B B B B"],
	"c": ["C C C C C", "C        ", "C        ", "C        ", "C C C C C"],
	"d": ["D D D D  ", "D      D ", "D       D", "D       D", "D D D D D"],
	"e": ["E E E E E", "E        ", "E E E E  ", "E        ", "E E E E E"],
	"f": ["F F F F F", "F        ", "F F F    ", "F        ", "F        "],
	"g": [" G G G G ", "G        ", "G    G G ", "G       G", " G G G G "],
	"h": ["H       H", "H       H", "H H H H H", "H       H", "H       H"],
	"i": ["  I I I  ", "    I    ", "    I    ", "    I    ", "  I I I  "],
	"j": ["  J J J J", "     J   ", "     J   ", "     J   ", "  J J    "],
	"k": ["K       K", "K     K  ", "K K K    ", "K     K  ", "K       K"],
	"l": ["L        ", "L        ", "L        ", "L        ", "L L L L L"],
	"m": ["M       M", "MM     MM", "M M   M M", "M  M M  M", "M   M   M"],
	"n": ["N       N", "N N     N", "N   N   N", "N     N N", "N       N"],
	"o": ["O O O O O", "O       O", "O       O", "O       O", "O O O O O"],
	"p": ["P P P P P", "P       P", "P P P P P", "P        ", "P        "],
	"q": ["  Q Q Q  ", " Q     Q ", "Q       Q", " Q    QQ ", "  Q Q QQQ"],
	"r": [" R R R R ", "R       R", "R  R R R ", "R     R  ", "R       R"],
	"s": ["  S S S S", "S        ", "S S S S S", "        S", "S S S S  "],
	"t": ["T T T T T", "    T    ", "    T    ", "    T    ", "    T    "],
	"u": ["U       U", "U       U", "U       U", "U       U", " U U U U "],
	"v": ["V       V", " V     V ", "  V   V  ", "   V V   ", "    V    "],
	"w": ["W       W", "W   W   W", "W  W W  W", "W W W W W", " W  W  W "],
	"x": ["X       X", "  X   X  ", "    X    ", "  X   X  ", "X       X"],
	"y": ["Y       Y", "  Y   Y  ", "    Y    ", "    Y    ", "    Y    "],
	"z": ["Z Z Z Z Z", "      Z  ", "    Z    ", "  Z      ", "Z Z Z Z Z"],
	"1": ["    1    ", "   11    ", "  1 1    ", "    1    ", "  1 1 1  "],
	"2": ["2 2 2 2 2", "        2", "2 2 2 2 2", "2        ", "2 2 2 2 2"],
	"3": ["3 3 3 3 3", "        3", "  3 3 3 3", "        3", "3 3 3 3 3"],
	"4": ["4       4", "4       4", "4 4 4 4 4", "        4", "        4"],
	"5": ["5 5 5 5 5", "5        ", "5 5 5 5 5", "        5", "5 5 5 5 5"],
	"6": ["6 6 6 6 6", "6        ", "6 6 6 6 6", "6       6", "6 6 6 6 6"],
	"7": ["7 7 7 7 7", "       7 ", "      7  ", "    777  ", "    7    "],
	"8": ["  8 8 8  ", "8       8", "  8 8 8  ", "8       8", "  8 8 8  "],
	"9": ["  9 9 9  ", "9       9", "9 9 9 9 9", "        9", "9 9 9 9  "],
	"0": ["  0 0 0  ", "0       0", "0       0", "0       0", "  0 0 0  "],
	" ": ["         ", "         ", "         ", "         ", "         "],
}

def console_writer(message):
	length = len(message)
	message = str(message).lower()
	cycles = length // 7
	if length % 7:
		cycles += 1

	for i in range(cycles):
		index = i * 7
		if index >= length:
			break

		for j in range(5):
			line = ""
			for k in range(7):
				letter_index = index + k
				if letter_index >= length:
					continue
				letter = message[letter_index]
				line += "  "
				if letter in letters.keys():
					line += letters[letter][j]
				else:
					line += letters[" "][j]
			print(line)
		print("\n")


if __name__ == '__main__':
	console_writer("Katitech")
