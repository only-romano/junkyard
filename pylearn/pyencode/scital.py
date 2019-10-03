"""
Scital cipher

# Encode
scital(message, shift)

# Decode
for shift in range(1, max_shift):
    scital(message, shift, True)

message: str, message to encode/decode
shift: int, number of columns
max_shift: int, maximum number of columns if number is unknown

"""

def scital(message, base=6, decode=False):
    length = len(message)
    max_index = length - 1
    result = ""

    if decode:
    	reminder = length % base
    	column = length // base
    	if reminder:
    		column += 1
    	reminder = length % column
    	switcher = base * reminder
        index = 0

        while len(result) < length:
        	result += message[index]

        	if index < switcher:
        		index += base
        	else:
        		index += base - 1

        	if index > max_index:
        		index = index - max_index
    else:
    	columns = max_index // base + 1
    	current_row = 0
        for i in range(columns):
            for index in range(current_row, length, columns):
                result += message[index]
            current_row += 1

    return result


if __name__ == "__main__":
    from random import randint

    message = "Test string with dynamic length: " + "test" * randint(1,3)
    encoded = scital(message, randint(2, 14))

    print("""# 1. Encoding

message = "%s"
encoded = scital(message, randint(2, 14))
print(encoded)

>>> %s

2. Decoding

for shift in range(2, 14):  # range of shifts to check
  print(scital(encoded, shift))\n""" % (message, encoded))

    for i in range(2, 14):
        print('>>> ' + scital(encoded, i, True) + ' (base ' + str(i) + ')')
