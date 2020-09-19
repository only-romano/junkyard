import multiprocessing as mp
import threading, queue
import time

# multiprocessing washer
def washer(dishes:list, output:"queue") -> None:
    for dish in dishes:
        print(f"Washing {dish} dish")
        output.put(dish)

def dryer(input:"queue") -> None:
    while True:
        dish = input.get()
        print(f"Drying {dish} dish")
        input.task_done()


# threading
def do_this(what:str) -> None:
    whoami(what)

def whoami(what:str) -> None:
    print(f"Thread {threading.current_thread()} says: {what}")


# threading washer
def washer_t(dishes:list, dish_queue:'queue') -> None:
    for dish in dishes:
        print(f"Washing {dish}")
        time.sleep(5)
        dish_queue.put(dish)

def dryer_t(dish_queue:'queue') -> None:
    while True:
        dish = dish_queue.get()
        print(f"Drying {dish}")
        time.sleep(10)
        dish_queue.task_done()

if __name__ == '__main__':
    dish_queue = mp.JoinableQueue()
    dryer_proc = mp.Process(target=dryer, args=(dish_queue,))
    dryer_proc.daemon = True
    dryer_proc.start()

    dishes = ['salad', 'bread', 'entree', 'desert']
    washer(dishes, dish_queue)
    dish_queue.join()

    whoami("I'm the main program")
    for n in range(4):
        p = threading.Thread(target=do_this, args=(f"I'm function {n}",))
        p.start()

    dish_queue_t = queue.Queue()
    for n in range(2):
        dryer_thread = threading.Thread(target=dryer_t, args=(dish_queue_t,))
        dryer_thread.start()
    dishes_t = ['salad_t', 'bread_t', 'entree_t', 'desert_t']
    washer_t(dishes_t, dish_queue_t)
    dish_queue_t.join()
