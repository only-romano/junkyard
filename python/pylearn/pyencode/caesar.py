"""
Ceasar cipher

# Encode
ceasar(message, shift)

# Decode
for shift in range(1, max_shift):
    ceasar(message, shift, True)

message: str, message to encode/decode
shift: int, value to shift characters
max_shift: int, value of maximum shift if shift value unknown
"""

def ceasar(message, shift=3, decode=False):
    length = len(message)
    result = ""

    def get_range(char_ord):
        if char_ord in range(65, 91):
            return { "min": 65, "max": 90, "len": 26 }
        elif char_ord in range(97, 123):
            return { "min": 97, "max": 122, "len": 26 }
        elif char_ord in range(48, 58):
            return { "min": 48, "max": 57, "len": 10 }
        elif char_ord in range(1040, 1072):
            return { "min": 1040, "max": 1071, "len": 32 }
        elif char_ord in range(1072, 1104):
            return { "min": 1072, "max": 1103, "len": 32 }
        return char_ord

    def find_code(char, shift):
        char_ord = ord(char)
        if char_ord == 1105:
            char_ord = 1077
        elif char_ord == 1025:
            char_ord = 1045
        range_ord = get_range(char_ord)
        if type(range_ord) == int:
            return char_ord

        new_char_ord = char_ord + shift
        while new_char_ord > range_ord["max"]:
            new_char_ord -= range_ord["len"]
        while new_char_ord < range_ord["min"]:
            new_char_ord += range_ord["len"]
        return new_char_ord


    if decode:
        for i in range(length):
            result += chr(find_code(message[i], -shift))
    else:
        for i in range(length):
            result += chr(find_code(message[i], shift))

    return result


if __name__ == "__main__":
    message = "Greka goes across the river, Greka sees a cancer there"
    encoded = ceasar(message, 30)
    print(encoded, ceasar(encoded, 30, True))
