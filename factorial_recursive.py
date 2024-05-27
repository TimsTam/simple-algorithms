# Computes the factorial or the input number using a recursive approach.
# Factorial of a number is the product of all positive integers less than or equal to n.
# 5! = 5× 4×3×2×1=120.

num = int(input("Enter Number"))


def factorial(n, accumulator):
    # n = the current number being processed
    # accumulator = the accumulated product
    if n > 1:
        accumulator = accumulator * (n-1)
        return factorial(n-1, accumulator)
    else:
        return accumulator


print(factorial(num, num))
