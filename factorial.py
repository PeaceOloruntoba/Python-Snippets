# https://github.com/PeaceOloruntoba
n = int(input("Enter a number to find it's factorial: "))

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))
# 2024 Peace Oloruntoba
