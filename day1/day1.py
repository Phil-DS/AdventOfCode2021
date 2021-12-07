from day1_data import data1

# Part 1: Iterate over each one in turn, ignoring the last one, and comparing it to its next
print(sum(int(data1[i+1] > data1[i]) for i in range(len(data1)-1)))

# Part 2: Like before, but to 3 before the end, and using slices+sum in place of the direct indexes
print(sum(int(sum(data1[i+1:i+4]) > sum(data1[i:i+3])) for i in range(len(data1)-3)))
