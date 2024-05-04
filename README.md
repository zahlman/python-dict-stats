# python-dict-stats
Quick &amp; dirty analysis of Python dict performance characteristics across versions

## Installation and usage

Clone the repository, then run `./generate.sh` (assumes Linux).

The `versions.txt` file lists versions of Python to try. The script will assume that the corresponding Python environments can be found like "python{version}".

An `output/` folder will appear with summary reports for each Python version, and a CSV file comparing all the results.
