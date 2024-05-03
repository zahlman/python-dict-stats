import itertools
from sys import getsizeof as memsize


def resizes(keys):
    base = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
    start_size = memsize(base)
    for k in keys:
        del base[k]
    base['f'] = 6
    return memsize(base) > start_size


# Determine when the dict resizes if 0 or more keys are deleted from a 5-key
# dict and then a new key is added.
def display_resizes(format_string):
    for key_count in range(6):
        trials = list(itertools.combinations('abcde', key_count))
        fails = [keys for keys in trials if resizes(keys)]
        print(format_string.format(key_count, len(fails), len(trials)))


# Determine base sizes of 0-, 5-, and 10-element dicts with varying types.
def display_sizes(format_strings):
    dicts = [
        {},
        {chr(a+ord('a')):a for a in range(5)},
        {a:chr(a+ord('a')) for a in range(5)},
        {chr(a+ord('a')):a for a in range(10)},
        {a:chr(a+ord('a')) for a in range(10)}
    ]
    for f, d in zip(format_strings, dicts):
        print(f.format(memsize(d)))


def get_resize_format(name):
    return {
        'raw': '{1}',
        'full': '{} keys removed: {}/{} resizes'
    }[name]


def get_size_format(name):
    return {
        'raw': ['{}'] * 5,
        'full': [
            'empty dict size: {}',
            '5-key letter-to-number dict size: {}',
            '5-key number-to-letter dict size: {}',
            '10-key letter-to-number dict size: {}',
            '10-key number-to-letter dict size: {}'
        ]
    }[name]


if __name__ == '__main__':
    format_name = 'full'
    display_sizes(get_size_format(format_name))
    print('') # support 2.7
    display_resizes(get_resize_format(format_name))
