#!/usr/bin/bash

mkdir -p output
for version in $(<versions.txt)
do
    python$version dictresize.py raw > output/raw$version.txt
    python$version dictresize.py full > output/full$version.txt
done
# Assuming `python` maps to a 3.6 or better version.
python make_csv.py
