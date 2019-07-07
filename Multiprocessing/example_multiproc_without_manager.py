import itertools as it
import os
import networkx as nx
import multiprocessing as mp

# Example of Multiprocessing with NUM_PROCS processes for each of them:
# 1) To process a list of pairs are passed. This list generates from from chunks_list
# 2) Global variable - G (it's graph). In each process we show, that it's not a copy of G
# 3) Do not use Memory Manager, because it takes too much resources. However it allows to edit shared variables


NUM_PROCS = 5  # number of processes
NUM_NODES = 2000  # number of nodes in Graph
p = 0.04  # probability of adding edge between two nodes


def chunks(lst, n):
    return [lst[i::n] for i in range(n)]


def find_paths(chunk):
    print('Graph in process', id(G), 'pid', os.getpid())  # Check that it's not a copy of graph
    print(mp.current_process(), 'Len of chunk:', len(chunk))
    print('')
    # print(chunk)
    for pair in chunk:  # for each pair run shortest_path function
        nx.shortest_path(G, source=pair[0], target=pair[1])


G = nx.fast_gnp_random_graph(n=NUM_NODES, p=p)
print('Graph in main process', id(G), 'pid', os.getpid())
print('Num of nodes:', G.number_of_nodes())
print('Num of edges:', G.number_of_edges())

pairs = list(it.combinations(G.nodes(), 2))  # Generate all possible combinations in graph
chunks_list = chunks(pairs, NUM_PROCS)  # split list pairs to NUM_PROCS parts, so each part go to its process
# returns list of lists. It contains NUM_PROCS elements

with mp.Pool(processes=NUM_PROCS) as p:
    p.map(find_paths, chunks_list)
