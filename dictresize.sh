#!/usr/bin/bash

for version in 2.7 3.5 3.6 3.7 3.8 3.9 3.10 3.11 3.12
do
    python$version dictresize.py > results$version.txt
done
