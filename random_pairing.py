# https://github.com/PeaceOloruntoba
import random

# Get input from the user
names_str = input("Enter a list of names separated by spaces: ")

# Split the input string into a list of names
names = names_str.split()

def create_random_groups(names):
    # Check if the number of names is even
    if len(names) % 2 != 0:
        print("Please provide an even number of names.")
        return
    
    # Shuffle the list of names randomly
    random.shuffle(names)
    
    # Create pairs of names
    groups = [(names[i], names[i + 1]) for i in range(0, len(names), 2)]
    
    # Display the randomly formed groups
    for group in groups:
        print(f"Group: {group[0]} and {group[1]}")

# Create and display randomly formed groups
create_random_groups(names)
# 2024 Peace Oloruntoba.
