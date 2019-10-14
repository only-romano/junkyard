# Adding line numbers to a python script                                         #  1
import fileinput                                                                 #  2
                                                                                 #  3
for line in fileinput.input(inplace=True):                                       #  4
    line = line.rstrip()                                                         #  5
    num = fileinput.lineno()                                                     #  6
    print('%-80s # %2i' % (line, num))                                           #  7
