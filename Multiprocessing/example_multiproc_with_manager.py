from functools import partial
import multiprocessing as mp


# Example with Memory Manager
# In this example you a list of values shared between different processes

def foo(shared_list, a):
    print(mp.current_process())
    shared_list.append(str(mp.current_process())) # append each process name to shared list
    # a = [i ** 4 for i in range(10 ** (a+4))]
    return a * 2


if __name__ == '__main__':
    manager = mp.Manager()
    shared_list = manager.list(['a', 'b', 'c'])
    list_parallel = [1, 2, 3, 4, 5] # each element of list will be send to some of processes
    # For example for 2 workers: 1 will go to 1st process, 2 will go to 2nd process, 3 will go to 1st process and so on

    with mp.Pool(processes=2) as pool:  # processes=2 - number of parallel processes
        results = pool.map(partial(foo, shared_list), list_parallel)
        print('Processing complete. Results: {}'.format(results))
    print(shared_list)
