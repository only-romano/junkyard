from time import sleep

# Alternative in Scratch: When clicked -> say "Heloo World!"
print('Hello World!')

from turtle import *

"""
Alternative in Scratch:
pen down ->
repeat "24" {
	move "10" steps ->
	turn R "15" degrees
} ->
pen up
  "cmd": ["/usr/bin/python3", "-u", "$file"],
  "file_regex": "^ ]*File \"(...*?)\", line ([0-9]*)",
  "selector": "source.python"
"""
pendown()

for n in range(24):
    forward(10)
    right(15)

penup()
sleep(1)
