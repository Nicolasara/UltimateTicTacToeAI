#!/bin/bash

cd ./tests

# make an empty array to store strings
declare -a arr

# Loop through all the Python files in the folder and put them in an array
for file in test_*.py; do
    # remove the .py extension
    file=${file%.py}
    arr+=("$file")
done

cd ..

# Loop through the array and run the Python files
for i in "${arr[@]}"; do

    echo "===================== Running $i ====================="
    python3 -m tests.$i
done
