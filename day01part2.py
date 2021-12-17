# AoC 2021 - holleyst
# Day 1 Part 2 (day01part2.py)
# https://adventofcode.com/2021/day/1#part2

# Read in depth measurements from input file (day01part2input.txt)
# Consider sums of a three-measurement sliding window. 
# How many sums are larger than the previous sum?

# read in depth measurements
input_file = "day01part2input.txt"
f = open(input_file, "r")
depth_list = [int(line.strip()) for line in f]
f.close()

# tally if larger than previous sum
ctr = 0
for idx, depth in enumerate(depth_list):
    if idx > 2 and (depth + depth_list[idx-1] + depth_list[idx-2] > depth_list[idx-1] + depth_list[idx-2] + depth_list[idx-3]):
        ctr = ctr + 1

# the answer
print(ctr)
