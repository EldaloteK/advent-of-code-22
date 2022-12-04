#!/usr/bin/env python3

# A = Rock, B = Paper, C = Scissors
# X = Rock, Y = Paper, Z = Scissors
# 1 Rock, 2 Paper, 3 Scissors
# 0 Lost, 3 Draw, 6 Won
# Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock

game_results = []
final_score_a = 0

score_map = {
    # lose
    ('A','Z'): 3,
    ('C','Y'): 2,
    ('B','X'): 1,

    # draw
    ('A','X'): 4,
    ('B','Y'): 5,
    ('C','Z'): 6,

    # win
    ('A','Y'): 8,
    ('B','Z'): 9,
    ('C','X'): 7,
}

with open("../input/2ab.txt", "r") as rpc_results:
    for r in rpc_results.readlines():
        pair = r.split()
        game_results.append(((pair[0]), (pair[1])))

# Part A
for g in game_results:
    final_score_a += score_map[g]
print(final_score_a)

# Part B

# X means you need to lose
# Y means you need to end the round in a draw
# Z means you need to win

final_score_b = 0

rpc_map = {
    'X': {
        'A': 3,
        'C': 2,
        'B': 1,
    },
    'Y': {
        'A': 4,
        'B': 5,
        'C': 6,
    },
    'Z': {
        'A': 8,
        'B': 9,
        'C': 7,
    }
}

for g in game_results:
    final_score_b += rpc_map[g[1]][g[0]]
print(final_score_b)