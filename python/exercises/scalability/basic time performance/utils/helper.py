import time
import matplotlib.pyplot as plt
import random

def get_exe_time(func, inputs: list[int] | list[str], *arg) -> list:
    exe_time = []
    
    for num in inputs:
        start = time.perf_counter()
        if len(arg):
            func(num, arg)
        else:
            func(num)
        end = time.perf_counter()
        exe_time.append(end - start)
    
    return exe_time


def draw_results(x, y1, y2):
    plt.figure(1)
    plt.subplot(211)
    plt.scatter(x, y1, label='Brute force')
    plt.xlabel('Size')
    plt.ylabel('Time')
    plt.title('Size vs Time')
    plt.legend()
    plt.grid(True)

    ymin, ymax = plt.ylim()

    plt.subplot(212)
    plt.scatter(x, y2, label='Optimized')
    plt.ylim([ymin, ymax])
    plt.show()

def get_random_list_of_nums_of_size(size: int) -> list[int]:
    return list(random.sample(range(0, size), size))
    pass