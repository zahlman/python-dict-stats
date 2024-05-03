#!/usr/bin/bash

mkdir -p output
for version in 2.7 3.5 3.6 3.7 3.8 3.9 3.10 3.11 3.12
do
    python$version dictresize.py $1 > output/$1$version.txt
done
