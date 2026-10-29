#!/bin/bash
# Call the CLI program (cli.py) once per combination of values.
PYTHON="${PYTHON:-python3}"

run() {
    echo "Running: $PYTHON ./TP3/associativity.py  --repetitions=$1"
    "$PYTHON" ./TP3/associativity.py  --repetitions=$1
}

run  10
run  500
run  1000
run  5000

run-llm() {
    echo "Running: $PYTHON ./TP3/associativity_llm.py  --repetitions=$1"
    "$PYTHON" ./TP3/associativity_llm.py  --repetitions=$1
}

run-llm  10
run-llm  500
run-llm  1000
run-llm  5000
