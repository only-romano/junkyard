import os

for i in range(100):
    file = open("file" + str(i), "w")
    file.write("file #" + str(i))
    file.close()

print("done")

for root, dirs, files in os.walk(os.curdir):
    for file in files:
        os.remove(file)
