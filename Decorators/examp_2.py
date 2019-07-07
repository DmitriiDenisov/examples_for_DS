from time import time
import math
from functools import wraps


# Example if we send an argument to decorator
def create_decorator(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            num_error = 0
            while True:
                try:  # try to run
                    start = time()
                    result = func(*args, **kwargs)
                    print('Time:{}'.format(time() - start))
                    return result
                except ValueError:
                    num_error += 1  # number of errors +1
                    if num_error > n:  # if n times => ValueError
                        raise ValueError

        return wrapper

    return decorator


# ----------------------------------
# TEST 1:
@create_decorator(2)
def stupid_func(*args, **kwargs):
    print('I\'m stupid function')
    print('And I got these *args:')
    for i in args:
        print(i, end='')
    print('')
    print('And I got these **kwargs:')
    for key in kwargs.values():
        print(key, end=' ')
    print('')


print('TEST_1:')
assert stupid_func(1, [1, 2, 3], 'AAAA', first='F!') is None
assert stupid_func.__name__ == 'stupid_func'


# ----------------------------------
# TEST 2:
@create_decorator(2)
def stupid_ret(x):
    return x + 1


print('TEST_2:')
assert stupid_ret(99) == 100
print('----------------------------------')


# ----------------------------------
# TEST 3: *args and **kwargs
@create_decorator(2)
def stupid_with_kw(a, b, x=None):
    print('I got variables: ', a, b)
    return x


print('TEST_3:')
assert stupid_with_kw(1, 2, x=210) == 210
print('----------------------------------')

# ----------------------------------------
# TEST 4: if we don't have opportunity to define function via def:
print('TEST_4:')
temp_dec = create_decorator(4)
pow_ = temp_dec(math.pow)
assert pow_(2, 3) == 8
