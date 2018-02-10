#!/usr/bin/env python3
"""
incentivizer.py
highwind

A tool for counting how many push-ups you've done, and determining the reward.
"""

from numpy import cos, pi

# Config TODO: move to its own file
COOKIE_COST = 10
EXERCISES = {
    "Push-Up": { "name": "push-ups", "value": 40, "goal": 120 },
    "Run": { "name": "meters of running", "value": 100, "goal": 2000 }
}


def ceil(n):
    return (n // 1) + 1

def score_repcount(goal, done):
    """Calculates your exercise score based on reps.

    Params:
        goal - the number of reps you aimed to do
        done - the reps you did
    
    Returns: a float between 0-2, granting you a score"""
    if done > 2 * goal:
        raise ValueError("Your goals are too low.")

    return 1 - cos((pi/2)*(done/goal))

def calculate_score(exercise):
    """Given an exercise, how well did the user score on that exercise?."""
    reps = int(input("How many %s did you do? " % exercise["name"]))
    return int(ceil(exercise["value"] * score_repcount(exercise["goal"], reps)))

def main():
    # TODO: add a main menu to select the kind of exercise you did
    # TODO: allow user to add exercises/other incentives
    # TODO: allow user to add rewards
    print("Welcome to the incentivizer.")
    score = calculate_score(EXERCISES["Push-Up"])
    c_score = int(input("How many cookies have you eaten? ")) * COOKIE_COST
    print("You've earned %i and spent %i of it on cookies." % (score, c_score), end=" ")
    print("You have %i remaining." % (score - c_score))


if __name__ == "__main__":
    main()
