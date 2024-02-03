# https://github.com/PeaceOloruntoba
n = int(input("Enter the number of fibonacci sequence you wish to find: "))

def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

print(fibonacci(n))
# 2024 Peace Oloruntoba