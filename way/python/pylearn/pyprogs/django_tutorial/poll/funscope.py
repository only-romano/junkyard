
count = 0

def func():
    global count
    global func
    count += 1
    buffer_func = func
    def func():
        buffer_func()
        buffer_func()


func()
print(count)

count = 0
func()
print(count)

count = 0
func()
print(count)

count = 0
func()
print(count)
