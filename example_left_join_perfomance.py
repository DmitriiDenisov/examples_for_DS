import pandas as pd
import string
import numpy as np
import random
import time
from tqdm import tqdm

N = 10 ** 5


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def generate_dataframe(N: int):
    INNs = []
    for i in tqdm(range(N)):
        INNs.append(id_generator())
    ids = np.random.permutation(N)
    id_person = random.sample(range(1, N * 10), N)
    return pd.DataFrame({'id': ids, 'INN': INNs, 'id_person': id_person}).set_index('id')


df1 = generate_dataframe(N)
df2 = generate_dataframe(N + 1000)
df1 = df1.rename(columns={'INN': 'INN_1', 'id_person': 'id_person_1'})
df2 = df2.rename(columns={'INN': 'INN_2', 'id_person': 'id_person_2'})

df1['index_1'] = df1.index.tolist()
df2['index_2'] = df2.index.tolist()

# Left join example
start = time.time()
df_new = pd.merge(df2, df1, left_on='index_2', right_on='index_1', how='left')
print('Time for Left Join:', time.time() - start)

# Join on index
start = time.time()
df = pd.concat([df1, df2], axis=1, join_axes=[df1.index])
print('Time for join on index:', time.time() - start)
