from statistics import mean, median, mode

def calculate_statistics(numbers):
    if not numbers:
        return None, None, None

    mean_value = mean(numbers)
    median_value = median(numbers)
    
    try:
        mode_value = mode(numbers)
    except StatisticsError:
        mode_value = "No unique mode"

    return mean_value, median_value, mode_value

# User Input
user_input = input("Enter a list of numbers separated by spaces: ")
try:
    user_numbers = [float(x) for x in user_input.split()]
    mean_result, median_result, mode_result = calculate_statistics(user_numbers)
    print(f"Entered Numbers: {user_numbers}")
    print(f"Mean: {mean_result}")
    print(f"Median: {median_result}")
    print(f"Mode: {mode_result}")
except ValueError:
    print("Invalid input. Please enter a list of numbers.")
