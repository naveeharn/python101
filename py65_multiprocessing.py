# Python multiprocessing

# multiprocessing 
# running tasks in parallel on different cpu cores, bypasses GIL used for threading

# multiprocessing   = better for cpu bound tasks (heavy cpu usage)
# multithreading    = better for io bound tasks (waiting around)

from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while count < num:
        count += 1

def main():

    print(cpu_count())

    process_1 = Process(target=counter, args=(100000000,))
    process_2 = Process(target=counter, args=(100000000,))
    process_3 = Process(target=counter, args=(100000000,))
    process_4 = Process(target=counter, args=(100000000,))

    process_1.start()
    process_2.start()
    process_3.start()
    process_4.start()

    process_1.join()
    process_2.join()
    process_3.join()
    process_4.join()

    print("Finished in : ", time.perf_counter(), " seconds")

if __name__ == '__main__':
    main()