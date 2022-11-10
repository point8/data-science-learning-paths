#! /bin/bash
set -e

for i in $(find notebooks -type f -name "*.ipynb" -not -name "*checkpoint.ipynb" | sort)
do
    echo "Stripping output of $i"
    nbstripout $i
done
