#!/usr/bin/env python3
from curses.ascii import isupper
import string

# + 1
lower_case_priority = list(string.ascii_lowercase)

# + 27
upper_case_priority = list(string.ascii_uppercase)

pack_total_a = 0

with open("../input/3ab.txt", "r") as packs_file:
    packs = [r.strip() for r in packs_file.readlines()]


# Part A
for p in packs:
    first_pack_max = int(len(p)/2)
    first_pack = set(p[0:first_pack_max])
    second_pack = set(p[first_pack_max: len(p)])
    pack_inter = first_pack.intersection(second_pack)
    pack_inter_str = list(pack_inter)[0]

    if isupper(pack_inter_str):
        pack_total_a += upper_case_priority.index(pack_inter_str)+27
    else:
        pack_total_a += lower_case_priority.index(pack_inter_str)+1

print(pack_total_a)

# Part B
part_total_b = 0
for p in packs[::3]:
    pack_a = set(packs[packs.index(p)])
    pack_b = set(packs[packs.index(p)+1])
    pack_c = set(packs[packs.index(p)+2])
    tria_inter = pack_a.intersection(pack_b, pack_c)
    pack_tria_inter_str = list(tria_inter)[0]

    if isupper(pack_tria_inter_str):
        part_total_b += upper_case_priority.index(pack_tria_inter_str)+27
    else:
        part_total_b += lower_case_priority.index(pack_tria_inter_str)+1

print(part_total_b)
