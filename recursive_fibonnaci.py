
n = int(input("Enter the sequence you wish to find: "))

def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Example Usage
result = fibonacci(6)
print(f"The {n}th Fibonacci number is: {result}")
