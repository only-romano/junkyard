import multiprocessing
import os
import time

def do_this(what:str) -> None:
    whoami(what)

def whoami(what:str) -> None:
    print(f"Process {os.getpid()} says: {what}")

def loopy(name:str) -> None:
    whoami(name)
    start = 1
    stop = 100000
    for num in range(start, stop):
        print(f"\tNumber {num} of {stop}. Honk!")
        time.sleep(1)

if __name__ == '__main__':
    whoami("I'm the main program")
    for n in range(4):
        p = multiprocessing.Process(target=do_this, args=(f"I'm functon {n}",))
        p.start()
    n = multiprocessing.Process(target=loopy, args=("loopy",))
    n.start()
    time.sleep(5)
    n.terminate()

