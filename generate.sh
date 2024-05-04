#!/usr/bin/bash

mkdir -p output
for version in 2.7 3.5 3.6 3.7 3.8 3.9 3.10 3.11 3.12
do
    python$version dictresize.py raw > output/raw$version.txt
    python$version dictresize.py full > output/full$version.txt
done
# Assuming `python` maps to a 3.6 or better version.
python make_csv.py
