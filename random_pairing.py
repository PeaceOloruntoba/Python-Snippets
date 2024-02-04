# https://github.com/PeaceOloruntoba
import random

names_str = input("Enter a list of names separated by spaces: ")
names = names_str.split()

def create_random_groups(names):
    if len(names) % 2 != 0:
        print("Please provide an even number of names.")
        return
    random.shuffle(names)    
    groups = [(names[i], names[i + 1]) for i in range(0, len(names), 2)]
    for group in groups:
        print(f"Group: {group[0]} and {group[1]}")

create_random_groups(names)
# 2024 Peace Oloruntoba.
