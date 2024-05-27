# Calculates and prints the number of rabbit pairs in the nth year using a Fibonacci sequence,
# where each year's pairs are the sum of the pairs from the previous two years.

num = int(input("Enter year: "))


def numRabbits(n, y1, y2):
    if n > 1:
        temp = y1
        y1 = y1 + y2
        y2 = temp
        return numRabbits(n-1, y1, y2)
    return y2


print(numRabbits(num, 1, 1))
