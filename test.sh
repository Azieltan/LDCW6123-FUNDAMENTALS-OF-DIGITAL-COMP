#!/bin/sh
set -eu
cd "$(dirname "$0")"
mkdir -p build
${CXX:-g++} -std=c++17 -Wall -Wextra -pedantic src/main.cpp -o build/movie_assistant
"${PYTHON:-python3}" tests/test_program.py build/movie_assistant
