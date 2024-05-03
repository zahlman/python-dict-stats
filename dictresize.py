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
def display_resizes():
    for key_count in range(6):
        trials = list(itertools.combinations('abcde', key_count))
        fails = [keys for keys in trials if resizes(keys)]
        print('{} keys removed: {}/{} resizes'.format(key_count, len(fails), len(trials)))


# Determine base sizes of 0-, 5-, and 10-element dicts with varying types.
def display_sizes():
    print('empty dict size: {}'.format(memsize({})))
    print('5-key letter-to-number dict size: {}'.format(
        memsize({chr(a+ord('a')):a for a in range(5)})
    ))
    print('5-key number-to-letter dict size: {}'.format(
        memsize({a:chr(a+ord('a')) for a in range(5)})
    ))
    print('10-key letter-to-number dict size: {}'.format(
        memsize({chr(a+ord('a')):a for a in range(10)})
    ))
    print('10-key number-to-letter dict size: {}'.format(
        memsize({a:chr(a+ord('a')) for a in range(10)})
    ))


if __name__ == '__main__':
    display_sizes()
    print('') # support 2.7
    display_resizes()
