# AoC 2021
# Day 1 Puzzle 1 (day01puzzle1.py)
# https://adventofcode.com/2021/day/1

# Read in depth measurements from input file (day01puzzle1input.txt)
# How many measurements are larger than the previous measurement?

# read in depth measurements
input_file = "day01puzzle1input.txt"
f = open(input_file, "r")
depth_list = [int(line.strip()) for line in f]
f.close()

# tally if previous measurement is larger
ctr = 0
for idx, depth in enumerate(depth_list):
    if idx != 0 and depth > depth_list[idx-1]:
        ctr = ctr + 1

# the answer
print(ctr)

