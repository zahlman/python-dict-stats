# Unlike dictresize.py, this one is intended to run under 3.6+
# so that f-strings are available, etc.
import csv


with open('versions.txt') as v:
    versions = v.read().split()


def get_data(version):
    with open(f'output/raw{version}.txt') as f:
        return [l.strip() for l in f]


labels = [
    'version',
    'empty dict size',
    '5-key letter-to-number dict size',
    '5-key number-to-letter dict size',
    '10-key letter-to-number dict size',
    '10-key number-to-letter dict size',
    '',
    'resizes if 0 keys removed',
    'resizes if 1 key removed',
    'resizes if 2 keys removed',
    'resizes if 3 keys removed',
    'resizes if 4 keys removed',
    'resizes if 5 keys removed'
]


with open('output/results.csv', 'w') as f:
    w = csv.writer(f)
    # Tag versions with a ".x" patch version so that CSV viewers don't
    # mistake "3.10" as numeric and drop the zero.
    for row in zip(labels, *([f'{v}.x'] + get_data(v) for v in versions)):
        w.writerow(row)
