#!/bin/bash

rm -r ./dist

# read a version number and increment it
new_version=$(cat VERSION.txt | awk -F. -v OFS=. 'NF==1{print ++$NF}; NF>1{if(length($NF+1)>length($NF))$(NF-1)++; $NF=sprintf("%0*d", length($NF), ($NF+1)%(10^length($NF))); print}')
echo "New version number is: $new_version"

# setting a new version number
echo $new_version > VERSION.txt

# create a python package
python3 setup.py sdist bdist_wheel
