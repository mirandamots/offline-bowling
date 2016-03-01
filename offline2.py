'''
Created on Feb 18, 2016

@author: Miranda Motsinger

Scores games of bowling given lists of integers representing rolls
from std.in. Prints only the final score.
'''

import sys


def strike(roll):
    return roll == 10


def spare(roll_a, roll_b):
    return roll_a + roll_b == 10


for line in sys.stdin:

    list_of_rolls = map(int, line.split())
    total_score = 0
    roll_index = 0

    # Iterates and adds to total_score 10 times, once for each frame.
    # Keeps track of roll_index separately so we know where we are in
    # list_of_rolls.
    for frame_index in range(10):
        curr_r = list_of_rolls[roll_index]
        next_r = list_of_rolls[roll_index + 1]

        # list_of_rolls[roll_index+1] is the "next next roll."
        if strike(curr_r):
            total_score += curr_r + next_r + list_of_rolls[roll_index + 2]
            roll_index += 1
        elif spare(curr_r, next_r):
            total_score += curr_r + next_r + list_of_rolls[roll_index + 2]
            roll_index += 2
        else:
            total_score += curr_r + next_r
            roll_index += 2

    print(str(total_score))