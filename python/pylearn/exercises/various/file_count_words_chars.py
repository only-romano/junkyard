"""
Reads a file and returns the number of lines, words, and characters - similar to
the UNIX wc utility
"""

def py_wc(file):
    infile = open(file) #open file
    lines = infile.read().split("\n")

    # init counters
    line_count = len(lines)
    word_count = 0
    char_count = 0

    for line in lines:
        words = line.split()
        word_count += len(words)
        char_count += len(line)

    return line_count, word_count, char_count
