#!/bin/sh
set -eu
cd "$(dirname "$0")"
g++ -std=c++17 -Wall -Wextra -pedantic src/main.cpp -o movie_assistant
printf '1\n3\n1\n2\n' | ./movie_assistant | grep -q 'Orbit Station'
printf '2\n1\n2\n2\n' | ./movie_assistant | grep -q 'Coffee and Clouds'
printf '3\n2\n2\n2\n' | ./movie_assistant | grep -q 'Night Shift'
printf 'wrong\n9\n1\n3\n1\n2\n' | ./movie_assistant | grep -q 'Please enter a number from 1 to 3'
printf '1\n' | ./movie_assistant | grep -q 'Input ended. Goodbye.'
echo 'Five program scenarios passed.'
