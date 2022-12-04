#!/usr/bin/env python3

with open("../input/4ab.txt", "r") as assignments_file:
    assignments = [r.strip().split(',') for r in assignments_file.readlines()]
    assignments2 = [[tuple(map(int, k[0].split('-'))), tuple(map(int, k[1].split('-')))] for k in assignments]

# Part A
num_of_pairs_containing_other_total = 0
num_of_pairs_that_overlap_at_all = 0

for a in assignments2:
    # First range in tuple
    afs = a[0][0]
    afe = a[0][1]
    a_first_set = set(list(range(afs, afe+1)))

    # Second range in tuple
    a_second_start = a[1][0]
    a_second_end = a[1][1]
    a_second_set = set(list(range(a_second_start, a_second_end+1)))

    inter = a_first_set.intersection(a_second_set)

    if inter:
        num_of_pairs_that_overlap_at_all += 1
        if inter == a_first_set or inter == a_second_set:
            num_of_pairs_containing_other_total += 1

# Part A
print(num_of_pairs_containing_other_total)

# Part B
print(num_of_pairs_that_overlap_at_all)
