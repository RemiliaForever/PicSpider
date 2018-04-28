#!/bin/env bash

# Make sure what you are doing, this script run without any checking.


PREFIX='file name prefix'

# create file list
for f in $(ls ${PREFIX}\(${1}\)* -v)
do
    echo "file '${f}'" >> files.txt
done

cat files.txt

# merge
ffmpeg -f concat -safe 0 -i files.txt -c copy "${PREFIX}-${1}.flv"


# clean
rm ${PREFIX}\(${1}\)*
rm files.txt



