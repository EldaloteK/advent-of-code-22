#!/usr/bin/env python3

with open("../input/1a.txt", "r") as snacks:
    snacks = [r.strip().split('\n') for r in snacks.readlines()]
    snacks2 = [s[0] for s in snacks]

# Part A
totals = []
temp_sum = 0
for snack in snacks2:
    if snack == '':
        totals.append(temp_sum)
        temp_sum = 0
    
    else:
        temp_sum += int(snack)

sorted_totals = sorted(totals)
print(sorted_totals)

# Part B
last_three_elf_calories = sum(sorted_totals[-3:])

print(last_three_elf_calories)