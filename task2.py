from itertools import zip_longest

keys = input('Input list of keys :').replace(' ', '').split(',')
values = input('Input list of values :').replace(' ', '').split(',')


def lists_to_dict(k, v):
    res = {k: v for k, v in zip_longest(keys, values) if k is not None}
    print(res)


lists_to_dict(keys, values)
