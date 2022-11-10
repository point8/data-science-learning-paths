#! /bin/bash
set -e

for i in $(find notebooks/ -type f -name "*.ipynb" -not -name "*checkpoint.ipynb" -not -name "wip_*.ipynb" | sort)
do
    jupyter nbconvert --ExecutePreprocessor.timeout=600 --execute $i
done
