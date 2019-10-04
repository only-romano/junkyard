#! Visualisation of multiply threads working
import _thread
import time


def counter(thread_name, count, process):
    """Counter of thread tasks with different time"""
    count = count
    while count > 0:
        print("{}, tasks remained: {}".format(thread_name, count))
        count -= 1
        time.sleep(process)


def threads():
    """Run multiply threads"""
    try:
        _thread.start_new_thread(counter, ("Thread 1", 10, 2))
        _thread.start_new_thread(counter, ("Thread 2", 20, 0.5))
        _thread.start_new_thread(counter, ("Thread 3", 5, 4))
        _thread.start_new_thread(counter, ("Thread 4", 10, 0.1))
        _thread.start_new_thread(counter, ("Thread 5", 3, 10))
    except:
        print("Something goes wrong.")
    while 1:
        pass


if __name__ == "__main__":
    threads()
