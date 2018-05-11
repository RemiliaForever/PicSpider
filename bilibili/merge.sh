#!/bin/env bash

# Make sure what you are doing, this script run with little checking.

PREFIX='xxxxxxxxxxxx'
OUTPUT_PREFIX='xxxxxxxxxxxxx'
SEARCH_RANGE=128

_merge() {
# create file list
list=$(ls ${PREFIX}\(${1}\)* -v 2>/dev/null)
if [[ -z "${list}" ]]; then
    >&2 echo "${1} : NotFound."
    return -1
fi

for f in ${list}
do
    if [[ ${f} =~ part$ ]]; then
        [[ -e files.txt ]] && rm files.txt
        echo "${1} : file is not download completed!"
        return -1
    fi
    echo "file '${f}'" >> files.txt
done

cat files.txt

# merge
ffmpeg -f concat -safe 0 -i files.txt -c copy "${OUTPUT_PREFIX}-${1}.flv"


# clean
rm ${PREFIX}\(${1}\)*
rm files.txt

}

if [[ -n "${1}" ]]; then
    return _merge $1
else
    for i in $(seq 1 ${SEARCH_RANGE}); do
        _merge $i 2>/dev/null
    done
fi
