#!/bin/bash

ntasks=(1 5 10 50 100 150 200 250 300)
#ntasks=(10 50 100 200 300 400 500 600 700 800 900 1000 2000 3000 4000 5000 6000 7000 8000 9000 10000)

for n in "${ntasks[@]}"; do
  go run "$PWD/tests_go/main.go" -n $n
  python "$PWD/tests_python/test_multithreading.py" -n $n
  python "$PWD/tests_python/test_multiprocessing.py" -n $n
done

python3 "$PWD/plot.py"