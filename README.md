# python-dict-stats
Quick &amp; dirty analysis of Python dict performance characteristics across versions

## Installation and usage

Clone the repository, then run `./generate.sh` (assumes Linux).

The `versions.txt` file lists versions of Python to try. The script will assume that the corresponding Python environments can be found like "python{version}".

An `output/` folder will appear with summary reports for each Python version, and a CSV file comparing all the results.

The results should look something like:

| version | 2.7.x | 3.5.x | 3.6.x | 3.7.x | 3.8.x | 3.9.x | 3.10.x | 3.11.x | 3.12.x |
| - | - | - | - | - | - | - | - | - | - |
| empty dict size | 280 | 288 | 240 | 248 | 64 | 64 | 64 | 64 | 64 |
| 5-key letter-to-number dict size | 280 | 288 | 240 | 248 | 232 | 232 | 232 | 184 | 184 |
| 5-key number-to-letter dict size | 280 | 288 | 240 | 248 | 232 | 232 | 232 | 224 | 224 |
| 10-key letter-to-number dict size | 1048 | 480 | 368 | 376 | 360 | 360 | 360 | 272 | 272 |
| 10-key number-to-letter dict size | 1048 | 480 | 368 | 376 | 360 | 360 | 360 | 352 | 352 |
|  |  |  |  |  |  |  |  |  |  |
| resizes if 0 keys removed | 1 | * | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| resizes if 1 key removed | 5 | * | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| resizes if 2 keys removed | 10 | * | 10 | 10 | 10 | 10 | 10 | 10 | 10 |
| resizes if 3 keys removed | 10 | * | 0 | 0 | 0 | 0 | 10 | 10 | 10 |
| resizes if 4 keys removed | 5 | * | 0 | 0 | 0 | 0 | 5 | 5 | 5 |
| resizes if 5 keys removed | 0 | * | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

(The resize results for Python 3.5 are not consistent between runs.)

The first set of rows shows the size in bytes (as reported by `sys.getsizeof`) for the specified dicts, created directly from literals (e.g. the empty dict is created by `{}`).
This does not count the size of the key or value objects themselves.

For the second set of rows: first, a dict is created with 5 key-value pairs; then some number of keys is `del`d; then a key is added. Each possible combination of keys to remove is tried, and the code reports how many combinations result in the dict being resized. (N.B. Across all versions of Python, the smallest hash table has 8 entries, and two-thirds of table entries (so, 5) may be used before a table resize is triggered. However, deleting keys may or may not "make room" for the sixth key to be added, depending on the implementation.)
