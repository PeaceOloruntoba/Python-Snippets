# https://github.com/PeaceOloruntoba
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)

# User Input
user_input = input("Enter a list of numbers separated by spaces: ")
try:
    user_array = [int(x) for x in user_input.split()]
    sorted_array = quicksort(user_array)
    print(f"Original Array: {user_array}")
    print(f"Sorted Array: {sorted_array}")
except ValueError:
    print("Invalid input. Please enter a list of numbers.")
