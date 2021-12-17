# AoC 2021 - holleyst
# Day 2 Part 1 (day02part1.py)
# https://adventofcode.com/2021/day/2

# Your horizontal position and depth both start at 0.
# Calculate the horizontal position and depth you would have after following the planned course. 
# What do you get if you multiply your final horizontal position by your final depth?

# read in commands
input_file = "day02part1input.txt"
f = open(input_file, "r")
cmd_list = [line.strip() for line in f]
f.close()

# start position
x = 0
y = 0

# process each command
for item in cmd_list:
    cmd = item.split(' ')
    if cmd[0] == "forward":
        x = x + int(cmd[1])
    elif cmd[0] == "down":
        y = y + int(cmd[1])
    else:
        y = y - int(cmd[1])

# multiply final horizontal position by depth
print(x*y)
