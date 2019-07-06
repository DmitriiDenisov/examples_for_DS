from itertools import islice


def split_every(n, iterable):
    iter_ = iter(iterable)
    piece = list(islice(iter_, n))
    while piece:
        yield piece
        piece = list(islice(iter_, n))


for j, i in enumerate(split_every(11, range(100))):
    print(i)
