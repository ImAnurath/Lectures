import threading
import multiprocessing
import time
import random
def sum_of_squares(numbers, result, index):
    result[index] = sum(x ** 2 for x in numbers)

def multi_threaded_sum_of_squares(numbers):
    num_threads = 4
    chunk_size = len(numbers) // num_threads
    threads = []
    results = [0] * num_threads

    for i in range(num_threads):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i != num_threads - 1 else len(numbers)
        thread = threading.Thread(target=sum_of_squares, args=(numbers[start:end], results, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return sum(results)
def multi_processed_sum_of_squares(numbers):
    num_processes = 4
    chunk_size = len(numbers) // num_processes
    manager = multiprocessing.Manager()
    results = manager.list([0] * num_processes)
    processes = []

    for i in range(num_processes):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i != num_processes - 1 else len(numbers)
        process = multiprocessing.Process(target=sum_of_squares, args=(numbers[start:end], results, i))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    return sum(results)

if __name__ == "__main__": # Main Difference
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ln = [random.randint(1, 100) for _ in range(100000000)]
    start = time.time()
    print("Sum of squares:", multi_threaded_sum_of_squares(ln))
    print("Threading time:", time.time() - start)
    start = time.time()
    print("Sum of squares:", multi_processed_sum_of_squares(ln))
    print("Multiprocessing time:", time.time() - start)