from time import time
from functools import wraps
import math


# Define a decorator
def my_decorator(func_to_measure):
    @wraps(func_to_measure)  # in order to print(stupid_func.__name__) prints name of func instead of decorator
    # Same for stupid_func.__doc__
    def wrapper(*args, **kwargs):
        start = time()
        result = func_to_measure(*args, **kwargs)
        print('Time:{}'.format(time() - start))
        return result

    return wrapper


# ----------------------------------
# TEST 1:
@my_decorator
def stupid_func(*args, **kwargs):
    """
    Does huge loop
    :param args: list of args
    :return: None
    """
    print('I\'m stupid function')
    print('And I got these *args:')
    for i in args:
        print(i, end='')
    print('')
    print('And I got these **kwargs:')
    for key in kwargs.values():
        print(key, end=' ')
    print('')
    for i in range(2 * 10 ** 7):
        pass


print('TEST_1:')
assert stupid_func(1, [1, 2, 3], 'AAAA', one='A', two='B') is None
assert stupid_func.__name__ == 'stupid_func'
print(stupid_func.__doc__)
print('----------------------------------')


# ----------------------------------
# TEST 2:
@my_decorator
def stupid_ret(x):
    return x + 1


print('TEST_2:')
assert stupid_ret(99) == 100
print('----------------------------------')


# ----------------------------------
# TEST 3: try *args and **kwargs
@my_decorator
def stupid_with_kw(a, b, x=None):
    print('I got variables: ', a, b)
    return x


print('TEST_3:')
assert stupid_with_kw(1, 2, x=210) == 210
print('----------------------------------')

# ----------------------------------------
# TEST 4: if we don't have opportunity to define function via def:
print('TEST_4:')
pow_ = my_decorator(math.pow)
assert pow_(2, 3) == 8
